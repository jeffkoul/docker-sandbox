
From this directory, build a Docker image based upon Dockerfile via:
```
docker build -t basic-image .
```

From this directory, create a new container based upon Docker image via
```
docker run -it -v ${PWD}/shared:/host/shared basic-image
```

From within container:
```
ll /var/stage
ll /host/shared
```

Detach from container via Ctrl-P Ctrl-Q


Misc:
```
docker ps
docker attach <imageid>
docker kill <imageid>
```
