#pull python image
FROM python:latest

#add trusting keys to apt for repositories
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -

#add google chrome 
RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'

#update apt
RUN apt-get -y update

#add and install google chrome
RUN apt-get install -y google-chrome-stable

#download chromedriver(downloads zip file containing chrome driver latest release)
RUN wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE`/chromedriver_linux64.zip

#unzip file
RUN apt-get install -yqq unzip
RUN unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/


#copy application in docker image
COPY . .

#install requirements
RUN pip3 install -r ./requirements.txt
RUN pip3 install selenium
RUN pip3 install webdriver_manager

#run application
CMD ["python","main_script.py"]
