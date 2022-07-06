FROM postgres:12.11

# copy `mydata` to the root/code
RUN mkdir -p /root/code
WORKDIR /root/code
COPY mydata .

# update the system
RUN apt-get update -y && apt-get install -y htop curl
RUN rm -rf /var/lib/apt/lists/*

# let's create database , username and password
ENV POSTGRES_DB docker_db
ENV POSTGRES_USER dockeruser
ENV POSTGRES_PASSWORD dockerpassword

# add init_db file
COPY init.sql /docker-entrypoint-initdb.d/