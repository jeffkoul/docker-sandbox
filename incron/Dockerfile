FROM centos:centos6
MAINTAINER jeffkoul@gmail.com

# create dirs
RUN mkdir -p /var/staging && \
    mkdir -p /var/incrondemo/any && \
    mkdir -p /var/incrondemo/in/move && \
    mkdir -p /var/incrondemo/in/close && \
    mkdir -p /var/incrondemo/out

# copy from host to container
COPY staging/* /var/staging/

# update yum
#RUN yum -y update

# update yum repos
RUN yum -y install wget
RUN wget https://dl.fedoraproject.org/pub/epel/6/x86_64/epel-release-6-8.noarch.rpm
RUN rpm -Uvh epel-release-6-8.noarch.rpm
RUN rm epel-release-6-8.noarch.rpm

# yum installations....
RUN yum -y install vim && \
    yum -y install cronie && \
    yum -y install inotify-tools && \
    yum -y install incron && \
    yum -y install supervisor


# configure supervisord
RUN cp /var/staging/supervisord.conf /etc/supervisord.conf

# register rules table with incrontab
RUN chmod a+rx /var/staging/move.sh && \
    incrontab /var/staging/simple.incrontab

CMD [ "/usr/bin/supervisord" ]
