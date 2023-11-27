# Use a base image with Hadoop client
FROM hadoop

ARG USERNAME=hadoop
ARG GROUPNAME=hadoop
ARG UID=1001
ARG GID=1001

# RUN echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME \
#  && chmod 0440 /etc/sudoers.d/$USERNAME \
#  && groupadd -g $GID $GROUPNAME \
#  && useradd -m -s /bin/bash -u $UID -g $GID $USERNAME

USER $USERNAME

# Set environment variables
ENV HIVE_VERSION 3.1.3
ENV HIVE_HOME /opt/hive
ARG HIVE_URL=https://archive.apache.org/dist/hive/hive-${HIVE_VERSION}/apache-hive-${HIVE_VERSION}-bin.tar.gz

# Install Hive
RUN sudo mkdir $HIVE_HOME  \ 
 && sudo chown $USERNAME:$GROUPNAME -R $HIVE_HOME \
 && curl -fsSL $HIVE_URL -o /tmp/hive.tar.gz \
 && tar -xf /tmp/hive.tar.gz -C $HIVE_HOME --strip-components 1 \
 && rm /tmp/hive*


# Thêm dòng sau vào Dockerfile
RUN wget https://repo1.maven.org/maven2/mysql/mysql-connector-java/8.0.23/mysql-connector-java-8.0.23.jar -P ${HIVE_HOME}/lib

# Set Hive environment variables
ENV PATH $PATH:${HIVE_HOME}/bin
ENV HIVE_CONF_DIR ${HIVE_HOME}/conf

ENV HADOOP_HOME /opt/hadoop
ENV PATH $PATH:$HADOOP_HOME/bin


# Copy configuration files
COPY --chown=$USERNAME:$GROUPNAME ./conf/hive-site.xml $HIVE_CONF_DIR/

# Expose Hive port
EXPOSE 10000


# Entry point
COPY entrypoint.sh /usr/local/sbin/entrypoint.sh
RUN sudo chmod a+x /usr/local/sbin/entrypoint.sh
ENTRYPOINT ["entrypoint.sh"]