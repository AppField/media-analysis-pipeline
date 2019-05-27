docker cp namenode:/etc/hadoop/core-site.xml hdfs_conf/core-site.xml
docker cp namenode:/etc/hadoop/hdfs-site.xml hdfs_conf/hdfs-site.xml
docker cp hdfs_conf/hdfs-site.xml nifi:/hdfs-site.xml
docker cp hdfs_conf/core-site.xml nifi:/core-site.xml
