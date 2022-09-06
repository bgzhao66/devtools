FROM scylladb/scylla-toolchain:fedora-34-20220622

COPY fedora.repo /etc/yum.repos.d/
RUN yum update 
RUN yum install -y psmisc sysstat net-tools lsof strace gdb valgrind 
RUN yum install -y vim ctags cscope curl wget tmux

