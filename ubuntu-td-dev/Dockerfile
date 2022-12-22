FROM ubuntu:20.04

ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update
RUN apt-get install -y gcc cmake build-essential git
RUN apt-get install -y pkg-config libjansson-dev libsnappy-dev liblzma-dev libz-dev unixodbc-dev unixodbc flex jq
RUN apt-get install -y psmisc sysstat net-tools lsof iputils-ping strace gdb valgrind
RUN apt-get install -y vim man-db
RUN yes | unminimize

RUN apt-get install -y python3 python3-pip
RUN apt-get install -y sudo

WORKDIR /root
COPY ./requirements.txt /root
RUN pip3 install -r ./requirements.txt

RUN apt-get install -y tmux ctags cscope
RUN apt-get install -y curl wget

RUN wget --continue https://golang.google.cn/dl/go1.18.3.linux-amd64.tar.gz && tar -xvf go1.18.3.linux-amd64.tar.gz -C /usr/local && rm -f go*.linux-amd64.tar.gz
ENV GO111MODULE=on
ENV GOPROXY=https://goproxy.cn,direct
ENV PATH=/usr/local/go/bin:$PATH

RUN apt-get install -y locales locales-all
ENV LC_ALL en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US.UTF-8
RUN pip3 install toml
RUN apt-get install -y xsltproc libavro-dev libjemalloc-dev
RUN apt-get update
RUN apt-get install -y rsync
RUN apt-get install -y iotop iftop
RUN apt-get install -y libgtest-dev

RUN apt-get update
RUN apt-get install -y tshark
RUN apt-get install -y iproute2
RUN pip3 uninstall -y taospy
RUN pip3 install taospy requests pexpect

RUN apt-get install -y unzip zip
