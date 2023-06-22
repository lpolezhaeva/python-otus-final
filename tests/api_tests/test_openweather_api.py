import pytest
import requests
from jsonschema import validate
from xml.etree import ElementTree
import allure

API_KEY = '51c9c17c706e140e1d067fd62f130720'


@allure.title("Weather fields in API response")
def test_api_json_schema(weather_api_base_url):
    res = requests.get(weather_api_base_url + f"/data/2.5/weather?lat=44.34&lon=10.99&appid={API_KEY}")

    schema = {
        "coord": {
            "lon": "number",
            "lat": "number",
        },
        "weather": [
            {
                "id": "number",
                "main": "string",
                "description": "string",
                "icon": "string"
            }
        ],
        "base": "string",
        "main": {
            "temp": "number",
            "feels_like": "number",
            "temp_min": "number",
            "temp_max": "number",
            "pressure": "number",
            "humidity": "number",
            "sea_level": "number",
            "grnd_level": "number"
        },
        "visibility": "number",
        "wind": {
            "speed": "number",
            "deg": "number",
            "gust": "number"
        },
        "rain": {
            "1h": "number"
        },
        "clouds": {
            "all": "number"
        },
        "dt": "number",
        "sys": {
            "type": "number",
            "id": "number",
            "country": "string",
            "sunrise": "number",
            "sunset": "number"
        },
        "timezone": "number",
        "id": "number",
        "name": "string",
        "cod": "number"
    }

    assert res.status_code == 200
    validate(instance=res.json(), schema=schema)


@allure.title("Current weather data - parameterized test: checking {lat} and {lon}")
@pytest.mark.parametrize("lat, lon", [(44.34, 10.99), (48.13, 11.58), (51.76, 55.097)])
def test_api_current_weather(lat, lon, weather_api_base_url):
    res = requests.get(weather_api_base_url + f"/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}")
    data = res.json()

    assert res.status_code == 200
    assert data["coord"] == {'lon': lon, 'lat': lat}


@allure.title("Built-in API request by city name - parameterized test: checking {city} and {country_code}")
@pytest.mark.parametrize("city, country_code", [("Moscow", "RU"), ("Berlin", "DE"), ("London", "GB")])
def test_api_by_city_name(city, country_code, weather_api_base_url):
    res = requests.get(weather_api_base_url + f"/data/2.5/weather?q={city}&appid={API_KEY}")
    data = res.json()

    assert res.status_code == 200
    assert data["name"] == city
    assert data["sys"]["country"] == country_code


@allure.title("Built-in API request by city ID - parameterized test: checking {city_id} and {name}")
@pytest.mark.parametrize("city_id, name", [("624805", "Naroch\'"), ("624861", "Myadzyel"), ("3077258", "Davle")])
def test_api_by_city_id(city_id, name, weather_api_base_url):
    res = requests.get(weather_api_base_url + f"/data/2.5/weather?id={city_id}&appid={API_KEY}")
    data = res.json()

    assert res.status_code == 200
    assert data["name"] == name


@allure.title("Built-in API request by ZIP code - parameterized test: checking {zip} and {country_code}")
@pytest.mark.parametrize("zip, country_code", [("94040", "US"), ("10115", "DE"), ("54500-000", "BR")])
def test_api_by_zip_code(zip, country_code, weather_api_base_url):
    res = requests.get(weather_api_base_url + f"/data/2.5/weather?zip={zip},{country_code}&appid={API_KEY}")
    data = res.json()

    assert res.status_code == 200
    assert data["sys"]["country"] == country_code


@allure.title("Multilingual support - Check French - parameterized test: checking {lang} and {name}")
@pytest.mark.parametrize("lang, name", [("fr", "Moscou"), ("ru", "Москва"), ("en", "Moscow"), ("de", "Moskau")])
def test_api_language_support(lang, name, weather_api_base_url):
    res = requests.get(weather_api_base_url + f"/data/2.5/weather?id=524901&lang={lang}&appid={API_KEY}")
    data = res.json()

    assert res.status_code == 200
    assert data["name"] == name


@allure.title("Format - XML - parameterized test: checking {name} and {country_code}")
@pytest.mark.parametrize("name, country_code", [("London", "GB"), ("Tokio", "JP"), ("Moscow", "RU"), ("Berlin", "DE")])
def test_api_format_xml(name, country_code, weather_api_base_url):
    res = requests.get(weather_api_base_url + f"/data/2.5/weather?q={name}&mode=xml&appid={API_KEY}")
    data = ElementTree.fromstring(res.content)

    assert res.status_code == 200
    assert data[0][1].text == country_code


@allure.title("Units of measurement - parameterized test: checking {lat} and {lon} and {units}")
@pytest.mark.parametrize("lat, lon", [(48, 11), (51, 55)])
@pytest.mark.parametrize("units", ["metric", "imperial"])
def test_api_units(lat, lon, units, weather_api_base_url):
    res = requests.get(weather_api_base_url + f"/data/2.5/weather?lat={lat}&lon={lon}&units={units}&appid={API_KEY}")
    data = res.json()

    assert res.status_code == 200
    assert data["coord"] == {'lon': lon, 'lat': lat}


@allure.title("Call back function for JavaScript code - parameterized test: checking {lat} and {lon}")
@pytest.mark.parametrize("lat, lon", [(44.34, 10.99), (48.13, 11.58), (51.76, 55.097)])
def test_api_callback_test(lat, lon, weather_api_base_url):
    """Current weather data"""

    res = requests.get(weather_api_base_url + f"/data/2.5/weather?lat={lat}&lon={lon}&callback=test&appid={API_KEY}")

    assert res.status_code == 200
    assert res.text.startswith("test(")


@allure.title("Error response - parameterized test: checking {lat} and {lon}")
@pytest.mark.parametrize("lat, lon", [(44.34, 10.99), (48.13, 11.58), (51.76, 55.097)])
def test_api_error(lat, lon, weather_api_base_url):
    res = requests.get(weather_api_base_url + f"/data/2.5/weather?lat={lat}&lon={lon}%%&appid={API_KEY}")
    data = res.json()

    assert res.status_code == 400
    assert data["message"] == 'wrong longitude'
