Article
https://habr.com/ru/companies/southbridge/articles/704208/


run:
docker-compose up -d

Войдём в контейнер через RabbitMQ
docker-compose exec rabbitmq bash


down:
docker-compose down

container re-create
rabbitmq_slurm kilex$ docker-compose up -d


docker-compose.yaml
version: "2.1"
services:
  rabbitmq:
    image: rabbitmq:3.10.7-management
    hostname: rabbitmq
    restart: always
    environment:
      - RABBITMQ_DEFAULT_USER=rmuser
      - RABBITMQ_DEFAULT_PASS=rmpassword
      - RABBITMQ_SERVER_ADDITIONAL_ERL_ARGS=-rabbit disk_free_limit 2147483648
    ports:
      - 15672:15672
      
