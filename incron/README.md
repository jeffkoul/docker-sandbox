
From this directory, build a Docker image based upon Dockerfile via:
```
docker build -t incrontab-image .
```

From this directory, create a new container based upon Docker image via
```
docker run -it incrontab-image
```

From within container:
```
service rsyslog status
service crond status
service incron status

# any fs event within /var/incrondemo/any triggers events
ll /var/incrondemo/any 

# files closed  within /var/incrondemo/in/close triggers a copy of that file
touch /var/incrondemo/in/close/whenIClose


# file moved to /var/incrondemo/in/close triggers a copy of that file
touch whenIMove
cp whenIMove /var/incrondemo/in/move/

ll /var/incrondemo/out/
tail -f /var/log/messages
tail -f /var/log/cron
```

Detach from container via Ctrl-P Ctrl-Q


Misc:
```
docker ps
docker exec -it <imageid> /bin/bash
docker kill <imageid>
```
