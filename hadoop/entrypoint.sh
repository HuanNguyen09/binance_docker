#!/bin/bash

# Start SSH daemon
sudo service ssh start

# Start Hadoop NameNode
# su -c "/opt/hadoop/bin/hdfs namenode" hdfs
./opt/hadoop/bin/hdfs namenode -format
./opt/hadoop/sbin/start-all.sh 

# exec /bin/bash
tail -f /dev/null
