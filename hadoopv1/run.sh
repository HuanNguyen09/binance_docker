#!/bin/bash

# Start SSH daemon
/usr/sbin/sshd -D &

# Start Hadoop NameNode
# su -c "/opt/hadoop/bin/hdfs namenode" hdfs
su -c "/opt/hadoop/sbin/start-all.sh" hdfs

exec $@