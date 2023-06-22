# Final project

The final project consists of two parts - API tests for OpenWeather and UI tests for OpenCart.

# 1. OpenWeather API Tests

This repository contains API tests for the OpenWeather API. The tests aim to validate the functionality and responses of various API endpoints.

## Table of Contents

- [Introduction](#introduction)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Running the Tests](#running-the-tests)

## Introduction

The OpenWeather API tests ensure the correctness and reliability of the OpenWeather API. These tests cover different scenarios and verify the expected behavior of the API responses.

## Prerequisites

Before running the tests, make sure you have the following prerequisites:

- Python 3.x installed on your system
- `pip` package manager installed

## Installation

To install the necessary dependencies, follow these steps:

1. Clone the repository:

   ```shell
   git clone https://github.com/your-username/openweather-api-tests.git
   ```

2. Navigate to the project directory:

   ```shell
   cd openweather-api-tests
   ```

3. Create a virtual environment (optional but recommended):

   ```shell
   python3 -m venv venv
   ```

4. Activate the virtual environment:

   - For Windows:

     ```shell
     venv\Scripts\activate.bat
     ```

   - For Unix or Linux:

     ```shell
     source venv/bin/activate
     ```

5. Install the required dependencies:

   ```shell
   pip install -r requirements.txt
   ```

## Configuration

Before running the tests, you need to configure the OpenWeather API key. Follow these steps:

1. Open the test file `test_openweather_api.py` in a text editor.

2. Replace the placeholder value `API_KEY` with your actual OpenWeather API key.

   ```python
   API_KEY = 'your-api-key'
   ```

3. Save the file.

## Running the Tests

To run the API tests, use the following command:

```shell
python -m pytest .\tests\api_tests\ 
```

This command will execute all the tests defined in the `test_openweather_api.py` file and display the test results in the console.

# 2. Opencart UI Tests
This repository contains UI tests for OpenCart using Selenium with Python. The tests aim to validate the functionality and behavior of the product page in the OpenCart e-commerce platform.

## Table of Contents

- [Introduction](#introduction)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Running the Tests](#running-the-tests)
- [License](#license)

## Introduction

The OpenCart Selenium UI tests ensure the correctness and reliability of the product page in the OpenCart e-commerce platform. These tests cover different scenarios and verify the expected behavior of the product forms, creation, editing, copying, and deletion.

## Prerequisites

Before running the tests, make sure you have the following prerequisites:

- Python 3.x installed on your system
- `pip` package manager installed
- Chrome WebDriver or Firefox WebDriver installed, depending on your preferred browser.

## Installation

To install the necessary dependencies, follow these steps:

1. Clone the repository:

   ```shell
   git clone https://github.com/your-username/opencart-selenium-ui-tests.git
   ```

2. Navigate to the project directory:

   ```shell
   cd opencart-selenium-ui-tests
   ```

3. Create a virtual environment (optional but recommended):

   ```shell
   python3 -m venv venv
   ```

4. Activate the virtual environment:

   - For Windows:

     ```shell
     venv\Scripts\activate.bat
     ```

   - For Unix or Linux:

     ```shell
     source venv/bin/activate
     ```

5. Install the required dependencies:

   ```shell
   pip install -r requirements.txt
   ```

## Running the Tests

To run the UI tests, use the following command:

```shell
python -m pytest .\tests\selenium_tests\ 
```

This command will execute all the tests and display the test results in the console.

To run the tests with the `pytest_addoption` function options, you can follow these instructions:

1. Run the tests using the `pytest` command and specify the options:

   ```shell
   pytest --browser chrome --drivers /path/to/chromedriver --url http://127.0.0.1:8081 --url_api https://api.openweathermap.org
   ```

   Replace the following options with your desired values:
   - `--browser`: Specify the browser to run the tests (e.g., `chrome`, `firefox`).
   - `--drivers`: Specify the path to the WebDriver executable.
   - `--url`: Specify the base URL of the OpenCart instance.
   - `--url_api`: Specify the Weather API endpoint URL.

   Example:
   ```shell
   pytest --browser chrome --drivers /home/user/chromedriver --url http://localhost:8080 --url_api https://api.openweathermap.org
   ```

   Note: Make sure to provide the correct paths and URLs for your setup.

2. The tests will be executed using the specified options, and the results will be displayed in the console.

   You can also add additional flags or options as needed for your testing environment.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.