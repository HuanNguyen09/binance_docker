# Use Ubuntu as the base image
FROM ubuntu:latest

# Install OpenJDK 8
RUN apt-get update \
    && apt-get install -y \
        ssh \
        openjdk-8-jdk \
        sudo \
        curl \
        gnupg \
        procps \
        python3 

# Clean up the package index and remove unnecessary files
RUN apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Set environment variables
ENV JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64
ENV PATH=$PATH:$JAVA_HOME/bin

# Command to run the Java application
CMD ["bash"]
