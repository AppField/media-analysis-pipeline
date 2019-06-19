#!/bin/sh
docker cp namenode:/etc/hadoop/core-site.xml nifi/core-site.xml
docker cp namenode:/etc/hadoop/hdfs-site.xml nifi/hdfs-site.xml
docker cp nifi/hdfs-site.xml nifi:/hdfs-site.xml
docker cp nifi/core-site.xml nifi:/core-site.xml
