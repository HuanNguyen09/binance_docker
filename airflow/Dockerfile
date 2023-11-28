# Use Ubuntu as the base image
FROM ubuntu-java8-base

# Set environment variables
ENV AIRFLOW_HOME=/opt/airflow
ENV DEBIAN_FRONTEND=noninteractive

ARG USERNAME=hadoop
ARG GROUPNAME=hadoop
ARG UID=1001
ARG GID=1001

# Install dependencies
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
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
RUN sudo pip3 install apache-airflow pandas python-binance pyspark datetime pytz apache-airflow[cncf.kubernetes]
ENV PATH=$PATH:/usr/local/airflow/bin

# # Initialize Airflow database
# RUN sudo airflow db migrate \
#  && sudo airflow users create \
#     --username admin \
#     --firstname Peter \
#     --lastname Parker \
#     --role Admin \
#     --email spiderman@superhero.org \
#     --password admin

# Expose the necessary ports
EXPOSE 8080

COPY ./code/* /code/
COPY ./dags/* /usr/local/lib/python3.10/dist-packages/airflow/example_dags/

# Set the working directory
WORKDIR $AIRFLOW_HOME

# Entry point
COPY entrypoint.sh /usr/local/sbin/entrypoint.sh
RUN sudo chmod a+x /usr/local/sbin/entrypoint.sh
ENTRYPOINT ["entrypoint.sh"]
