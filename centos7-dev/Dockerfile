FROM centos:centos7.9.2009

RUN yum install -y epel-release && yum update -y
RUN yum install -y gcc gcc-c++ make cmake3 git gdb valgrind vim && ln -sf /usr/bin/cmake3 /usr/bin/cmake
RUN yum install -y zlib-devel xz-devel snappy-devel jansson jansson-devel pkgconfig libatomic libstdc++-static

ENV LC_ALL en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US.UTF-8
