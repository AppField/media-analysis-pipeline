# Media Analysis Pipeline

## Summary

Our Capstone Project called "Media Analysis Pipeline" is used to collect various newspapers articles and store them for analysis. 

Currently there are three support news outletts:
- Die Presse
- Kronen Zeitung
- Unzenzusriert.at




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
