#!/bin/bash

# Start SSH daemon
sudo service ssh start
./opt/hadoop/bin/hdfs namenode -format
./opt/hadoop/sbin/start-all.sh 
./opt/hive/bin/schematool -initSchema -dbType mysql
./opt/hive/bin/hive --service metastore
# hive
# exec /bin/bash
tail -f /dev/null