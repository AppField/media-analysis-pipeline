# Media Analyse Pipeline

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


## Links

### Link to hadoop & spark medium article
https://medium.com/@ivanermilov/scalable-spark-hdfs-setup-using-docker-2fd0ffa1d6bf