# MICROSERVICES 
The repo created to proof interworking between microservices 
via HTTP protocol and via pipe (RabbitMQ broker).\
3 microservices are implemented based on docker-containers.

The repo contains 3 applications located in containers:
# Application1 (Django-based)
The app provides web-interface, send respective HTTP get request to app2

# Application2 (FLASK - based)
get HTTP "GET" request from app1, and dependence on logic either terminates it ,
either send request to app3 via pipe, using RabbitMQ message broker

# Application3 (Python script)
The app read message from Pipe, proceed logic and returns response via HTTP to app2.
App2 stores results in database.

# Run project : 
```shell
docker-compose build
```
```shell
docker-compose up -d
```

# Descripton and Screenshots
Description and Screenshots are attached in file 
Microservices_Screenshots.pdf

# License
MIT