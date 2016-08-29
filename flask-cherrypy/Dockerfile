FROM centos:centos6
MAINTAINER jeffkoul@gmail.com

# copy from host to container
COPY staging/ /var/staging/

# update yum
RUN rpm -ivh http://dl.fedoraproject.org/pub/epel/6/x86_64/epel-release-6-8.noarch.rpm
RUN yum -y update

# yum installations....
RUN yum -y install python 
RUN yum -y install python-devel
RUN yum -y install python-setuptools
RUN yum -y install python-pip

# pip installations....
RUN pip install --upgrade pip
RUN pip install flask
RUN pip install cherrypy

EXPOSE 80

CMD python /var/staging/webapp/server.py
