# docker-sandbox

## Docker Setup

### Centos 6

Verify OS version and architecture
```
uname -r
cat /etc/redhat-release
uname -r
```


Check for epel repo. wget version/architecture specific rpm if missing (6 / x86_64 shown below), and install
```
sudo yum repolist
wget https://dl.fedoraproject.org/pub/epel/6/x86_64/epel-release-6-8.noarch.rpm
sudo rpm -Uvh epel-release-6*.rpm
```


Install docker and start docker daemon, optionally choosing to start automaticlay at boot up

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


Setup 'docker' group for sudo-less execution
```
sudo groupadd docker
sudo usermod -aG docker <user>
```


Verify sudo-less execution after loging out/in
```
id <user>
groups <user>
docker run hello-world
``` 
