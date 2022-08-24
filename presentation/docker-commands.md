# Comandos usados na aula

- Criar uma imagem

  ```sh
  docker build -t dt-server .
  ```

- Listar as imagens disponíveis

  ```sh
  docker images
  ```

- Remover imagens

  ```sh
  docker rmi dt-server
  ```

- Executar container de maneira interativa

  ```sh
  docker run -it python:3-alpine [/bin/sh]
  ```

- Executar container em background

  ```sh
  docker run -d --name dtutor-postgres -e POSTGRES_PASSWORD=senha postgres:alpine
  ```

- Parar um container

  ```sh
  docker stop dtutor-postgres
  ```

- Iniciar um container

  ```sh
  docker start dtutor-postgres
  ```

- Remover um container mesmo estando em execução

  ```sh
  docker rm -f dtutor-postgres
  ```

- Criar volumes e redes

  ```sh
  docker volume create dtutor-volume
  ```

  ```sh
  docker network create dtutor-net
  ```

- Executar container em background com mapeamento de portas e volumes

  ```sh
  docker run -d --name dtutor-postgres --restart always -v dtutor-volume:/var/lib/postgresql/data -p 5430:5432 --network dtutor-net -e POSTGRES_PASSWORD=docker -e POSTGRES_USER=docker -e POSTGRES_DB=docker_tutor postgres:alpine
  ```

  ```sh
  docker run -d --name dtutor-server -p 8000:5000 --network dtutor-net -e POSTGRES_HOST=dtutor-postgres dt-server
  ```

- Ver containers em execução

  ```sh
  docker ps [-a]
  ```

- Ver consumo de recursos dos containers em execução

  ```sh
  docker stats
  ```

- Ver logs de containers em execução

  ```sh
  docker logs dtutor-server
  ```

- Atualizar configurações dos containers

  ```sh
  docker update --restart=no dtutor-postgres
  ```

---

- Iniciar containers com Docker Compose

  ```sh
  docker-compose up [-d]
  ```

- Ver logs dos containers com Docker Compose

  ```sh
  docker-compose logs [<containers>]
  ```

- Parar e remover containers com Docker Compose

  ```sh
  docker-compose down
  ```
