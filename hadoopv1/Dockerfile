# Sử dụng Ubuntu 18.04 làm base image
FROM ubuntu

# Cài đặt Java 8
RUN apt-get update && \
    apt-get install -y openjdk-8-jdk curl && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Thiết lập biến môi trường cho Java
ENV JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64
ENV PATH=$PATH:$JAVA_HOME/bin
ENV HADOOP_HOME=/opt/hadoop
ENV HADOOP_CONF_DIR=$HADOOP_HOME/etc/hadoop
ENV PATH=$HADOOP_HOME/sbin:$HADOOP_HOME/bin:$PATH
ENV LD_LIBRARY_PATH=$HADOOP_HOME/lib/native:$LD_LIBRARY_PATH
# Add hdfs user and group
RUN groupadd -r hdfs && useradd --no-log-init -r -g hdfs hdfs
# Download and install Hadoop
RUN mkdir /opt/hadoop && \
    curl -L https://downloads.apache.org/hadoop/common/hadoop-3.3.6/hadoop-3.3.6.tar.gz | tar xvz -C /opt/hadoop --strip-components=1

# Cấu hình Hadoop
COPY ./conf/core-site.xml $HADOOP_CONF_DIR/
COPY ./conf/hdfs-site.xml $HADOOP_CONF_DIR/
COPY ./conf/yarn-site.xml $HADOOP_CONF_DIR/
COPY ./conf/mapred-site.xml $HADOOP_CONF_DIR/
COPY ./conf/hadoop-env.sh $HADOOP_CONF_DIR/
RUN apt-get update && \
    apt-get install -y openssh-server && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Cấu hình SSH
RUN mkdir /var/run/sshd
RUN echo 'root:root' | chpasswd
RUN sed -i 's/PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd

# Mở cổng SSH
EXPOSE 22


# Tạo thư mục cho dữ liệu HDFS
RUN mkdir -p /hadoop/data/hdfs/namenode && \
    mkdir -p /hadoop/data/hdfs/datanode

# Chạy lệnh khởi động NameNode để khởi tạo metadata cho HDFS
RUN /opt/hadoop/bin/hdfs namenode -format

# Mở cổng cho NameNode và DataNode
EXPOSE 9870 9864

# CMD to start Hadoop NameNode when the container runs
# CMD ["/usr/sbin/sshd", "-D"] && su -c "/opt/hadoop/bin/hdfs namenode" hdfs

# Expose ports for Hive
EXPOSE 10000 9083

# CMD to start-all.sh after the container starts
# CMD ["/usr/sbin/sshd", "-D"] && su -c "/opt/hadoop/sbin/start-all.sh" hdfs
# CMD để khởi động SSH và Hadoop NameNode khi container chạy

ADD run.sh /run.sh
RUN chmod a+x /run.sh

CMD ["/run.sh"]
