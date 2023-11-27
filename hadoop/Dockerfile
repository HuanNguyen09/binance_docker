FROM ubuntu-java8-base

ARG USERNAME=hadoop
ARG GROUPNAME=hadoop
ARG UID=1001
ARG GID=1001

RUN echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME \
 && chmod 0440 /etc/sudoers.d/$USERNAME \
 && groupadd -g $GID $GROUPNAME \
 && useradd -m -s /bin/bash -u $UID -g $GID $USERNAME

USER $USERNAME

# ENV JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64/

# Hadoop
ARG HADOOP_VERSION=3.3.6
ARG HADOOP_URL=https://www.apache.org/dist/hadoop/common/hadoop-$HADOOP_VERSION/hadoop-$HADOOP_VERSION.tar.gz
ENV HADOOP_HOME=/opt/hadoop

# Install ssh-key
RUN ssh-keygen -t rsa -P '' -f ~/.ssh/id_rsa \
    && cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys \
    && chmod 0600 ~/.ssh/authorized_keys 

RUN sudo mkdir $HADOOP_HOME  \
 && sudo chown $USERNAME:$GROUPNAME -R $HADOOP_HOME \
 && curl -fsSL $HADOOP_URL -o /tmp/hadoop.tar.gz \
 && tar -xf /tmp/hadoop.tar.gz -C $HADOOP_HOME --strip-components 1 \
 && mkdir $HADOOP_HOME/logs \
 && rm /tmp/hadoop*

RUN sudo mkdir -p /home/hadoop/hdfs/namenode \
 && sudo mkdir -p /home/hadoop/hdfs/datanode \
 && sudo chown -R hadoop:hadoop /home/hadoop/hdfs 


ENV HADOOP_CONF_DIR=$HADOOP_HOME/etc/hadoop
ENV PATH=$HADOOP_HOME/sbin:$HADOOP_HOME/bin:$PATH
ENV LD_LIBRARY_PATH=$HADOOP_HOME/lib/native:$LD_LIBRARY_PATH


# Config
COPY --chown=$USERNAME:$GROUPNAME ./conf/core-site.xml $HADOOP_CONF_DIR/
COPY --chown=$USERNAME:$GROUPNAME ./conf/hdfs-site.xml $HADOOP_CONF_DIR/
COPY --chown=$USERNAME:$GROUPNAME ./conf/yarn-site.xml $HADOOP_CONF_DIR/
COPY --chown=$USERNAME:$GROUPNAME ./conf/mapred-site.xml $HADOOP_CONF_DIR/
COPY --chown=$USERNAME:$GROUPNAME ./conf/hadoop-env.sh $HADOOP_CONF_DIR/

# Entry point
COPY entrypoint.sh /usr/local/sbin/entrypoint.sh
RUN sudo chmod a+x /usr/local/sbin/entrypoint.sh
ENTRYPOINT ["entrypoint.sh"]

EXPOSE 9000 50010 50020 50070 50075 50090 9870