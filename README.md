# Media Analysis Pipeline

## Summary

Our Capstone Project called "Media Analysis Pipeline" is used to collect various newspapers articles and store them for analysis. 
The pipeline consits of various technologies, all of which run in containerized environments. THe containers are managed by Docker. 

Currently there are three support news outletts:
- [Die Presse](https://diepresse.com)
- [Kronen Zeitung](https://www.krone.at)
- [Unzenzusriert.at](https://www.unzensuriert.at)


#### Deployment
The minimum deployment consits of:
- one HDFS namenode
- one HDFS datanode
- one Apache zookeeper 
- one Apache Nifi instance
- two ElasticSearch container
- one Kibana container
- one Hue container

![alt text](etc/deployment.png "Deployment Diagramm")

#### Workflow
All of the workflow for getting the data, transforming it, saving raw data aswell as transformed and finally storing it in ElasticSearch for analysis, is managed by Apache Nifi.

![alt text](etc/workflow.png "Workflow Diagramm")

## Setup

Run:
```
docker-compose up
```
Then run hdfs_conf_script.sh to copy config files from hadopp to Nifi


## Open NiFi UI
To get NiFis port, simply run:
```
docker ps
```

Open `localhost:<NIFIPORT>`.


## Elasticsearch
To get Elasticsearch running execute this command on the host machine:
```
sudo sysctl -w vm.max_map_count=262144
```
This has to be done after every reboot

## Links

### Link to hadoop & spark medium article
https://medium.com/@ivanermilov/scalable-spark-hdfs-setup-using-docker-2fd0ffa1d6bf
