FROM apache/nifi

USER root

RUN apt-get update && apt-get upgrade -y \ 
    && apt-get install python3 -y \
    && apt-get install python3-pip -y \
    && apt-get install vim -y \
    && apt-get install firefox-esr -y

# install python modules
COPY ./requirements.txt /requirements.txt
RUN pip3 install -r /requirements.txt

# import existing workflow templates
#COPY ./templates/Test_Template.xml /opt/nifi/conf/templates/Test_Templte.xml

#import selenium/geckodriver with scraper
RUN mkdir selenium
COPY ./standard/. /opt/nifi/nifi-current/selenium/

USER nifi

EXPOSE 8080
