FROM apache/nifi

USER root

RUN apt-get update && apt-get upgrade -y \ 
    && apt-get install python3 -y \
    && apt-get install python3-pip -y \
    && apt-get install vim -y

# install python modules
COPY ./scrapper/requirements.txt /requirements.txt
RUN pip3 install -r /requirements.txt

# import existing workflow templates
#COPY ./workflows/test_workflow.xml /opt/nifi/conf/templates/Test_Workflow.xml

USER nifi

EXPOSE 8080