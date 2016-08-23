# docker-sandbox

## Docker Setup

### Centos 6


Check for epel repo, wget if missing and install rpm
```
sudo yum repolist
wget https://dl.fedoraproject.org/pub/epel/6/x86_64/epel-release-6-8.noarch.rpm
sudo rpm -Uvh epel-release-6*.rpm
```


Install docker and start docker dameon, optionally choosing to start automaticlay at boot up

```
sudo yum install docker-io
sudo service docker start
sudo chkconfig docker on
```


Verify installation
```
sudo docker images
sudo docker run hello-world
sudo docker images
```
