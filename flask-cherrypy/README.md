
From this directory, build a Docker image based upon Dockerfile via:
```
docker build -t flask-cherrypy-image .
```

From this directory, create a new container based upon Docker image via
```
docker run -it -p 443:80 flask-cherrypy-image
```

From container host, via either curl or browser:
```
http://localhost:443/static
http://localhost:443/static/subPath

http://localhost:443/api/things
http://localhost:443/api/thing/1
http://localhost:443/api/thing/2
http://localhost:443/api/thing/3
```

Detach from container via Ctrl-P Ctrl-Q


Misc:
```
docker ps
docker exec -it <imageid> /bin/bash
docker kill <imageid>
```
