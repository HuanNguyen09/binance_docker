# Use Ubuntu as the base image
FROM ubuntu-java8-base

# Set environment variables
ENV SUPERSET_HOME=/opt/superset
ENV DEBIAN_FRONTEND=noninteractive
ENV FLASK_APP=superset
ENV SUPERSET_CONFIG_PATH=$SUPERSET_HOME/superset_config.py

ARG USERNAME=hadoop
ARG GROUPNAME=hadoop
ARG UID=1001
ARG GID=1001

# Install dependencies
RUN apt-get update && apt-get install -y build-essential libssl-dev libffi-dev python3-dev python3-pip libsasl2-dev libldap2-dev default-libmysqlclient-dev redis-server \
    tzdata \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

# Create user and set permissions
RUN groupadd -g $GID $GROUPNAME \
 && useradd -m -s /bin/bash -u $UID -g $GID $USERNAME \
 && echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME \
 && chmod 0440 /etc/sudoers.d/$USERNAME

USER $USERNAME

# Install Apache Airflow
RUN sudo pip3 install --upgrade pip\
 && sudo pip install apache-superset 
# ENV PATH=$PATH:/usr/local/airflow/bin

RUN sudo pip install pyhive thrift thrift_sasl redis
# Expose the necessary ports
EXPOSE 8088

COPY ./conf/* $SUPERSET_HOME/

# Set the working directory
WORKDIR $SUPERSET_HOME

# Entry point
COPY entrypoint.sh /usr/local/sbin/entrypoint.sh
RUN sudo chmod a+x /usr/local/sbin/entrypoint.sh \
 && sudo chmod a+rw /opt/superset/

ENTRYPOINT ["entrypoint.sh"]
