# Use Alpine Linux with OpenJDK 8 as the base image
FROM alpine:latest

# Set environment variables
ENV JAVA_HOME=/usr/lib/jvm/java-1.8-openjdk
ENV PATH=$PATH:$JAVA_HOME/bin

# Install necessary packages
RUN apk add --update --no-cache \
    openjdk8 \
    bash \
    curl \
    && rm -rf /var/cache/apk/*

# Download and extract Hadoop binary
ENV HADOOP_VERSION=3.3.1
ENV HADOOP_HOME=/opt/hadoop
RUN mkdir -p ${HADOOP_HOME} && \
    curl -sSL https://www.apache.org/dist/hadoop/common/hadoop-${HADOOP_VERSION}/hadoop-${HADOOP_VERSION}.tar.gz \
    | tar -xz -C ${HADOOP_HOME} --strip-components=1

# Set Hadoop environment variables
ENV HADOOP_HOME=${HADOOP_HOME}
ENV HADOOP_CONF_DIR=${HADOOP_HOME}/etc/hadoop
ENV PATH=$PATH:${HADOOP_HOME}/bin

# Create a non-root user for Hadoop
RUN addgroup -S hadoop && adduser -S -G hadoop hadoop

# Set user permissions
RUN chown -R hadoop:hadoop ${HADOOP_HOME}

# Switch to the non-root user
USER hadoop

# Expose Hadoop ports
EXPOSE 9870 8088

# Set working directory to Hadoop home
WORKDIR ${HADOOP_HOME}

# Start Hadoop services
CMD ["bash"]
