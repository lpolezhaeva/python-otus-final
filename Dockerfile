# FROM python:3.10.2-bullseye
FROM python:3.10.2

RUN apt-get update -y
# We need wget to set up the PPA and xvfb to have a virtual screen and unzip to install the Chromedriver
RUN apt-get install -y wget xvfb unzip iputils-ping curl
# Set up the Chrome PPA
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list
# Update the package list and install chrome
RUN apt-get update -y
RUN apt-get install -y google-chrome-stable
# Set up Chromedriver Environment variables
ENV CHROMEDRIVER_VERSION 114.0.5735.90
# ENV CHROMEDRIVER_VERSION 113.0.5672.63
ENV CHROMEDRIVER_DIR /chromedriver
RUN mkdir $CHROMEDRIVER_DIR
# Download and install Chromedriver
RUN wget -q --continue -P $CHROMEDRIVER_DIR "http://chromedriver.storage.googleapis.com/$CHROMEDRIVER_VERSION/chromedriver_linux64.zip"
RUN unzip $CHROMEDRIVER_DIR/chromedriver* -d $CHROMEDRIVER_DIR
# Put Chromedriver into the PATH
ENV PATH $CHROMEDRIVER_DIR:$PATH

# set display port to avoid crash
ENV DISPLAY=:99

WORKDIR /app

ADD requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY helpers.py .
COPY conftest.py .
COPY pytest.ini .
COPY tests/ tests/
COPY page_objects/ page_objects/

WORKDIR tests
CMD ["pytest"]
