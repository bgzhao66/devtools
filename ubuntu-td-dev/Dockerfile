FROM ubuntu:20.04

ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update
RUN apt-get install -y gcc cmake build-essential git
RUN apt-get install -y pkg-config libjansson-dev libsnappy-dev liblzma-dev libz-dev unixodbc-dev unixodbc flex jq
RUN apt-get install -y psmisc sysstat net-tools lsof iputils-ping strace gdb valgrind
RUN apt-get install -y vim man-db
RUN yes | unminimize

WORKDIR /root
COPY . /root
RUN apt-get install -y python3 python3-pip
RUN pip3 install -r ./requirements.txt
