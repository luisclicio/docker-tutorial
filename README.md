# Introdução a Docker para desenvolvedores

Conteúdo e exemplo produzidos por [Luís Clício](https://github.com/DarkTechLC)
para ministrar uma aula de introdução a [Docker](https://docs.docker.com/get-started/overview/)
na disciplina de Programação Orientada a Objetos II do curso de Sistemas de
Informação na Universidade Federal do Piauí (UFPI).

## Tópicos tratados

- O que é e quais as vantagens de usar Docker
- O que são imagens e como gerenciá-las
- O que são containers e como gerenciá-los
- Como orquestrar containers com Docker Compose

## Conteúdo produzido

- [Slides da apresentação](presentation/docker-slides.pdf)
- [Comandos usados na apresentação](presentation/docker-commands.md)

## Como executar o exemplo

> **Obs.:** é necessário ter o Docker e o Docker Compose instalados para prosseguir com os próximos passos.

O exemplo consiste em uma aplicação web extremante simples construída com o
framework [Flask](https://flask.palletsprojects.com/en/2.2.x/), escrito em Python,
e que armazena os dados com [PostgreSQL](https://www.postgresql.org). Para
executá-lo, siga as etapas a seguir:

- Clone o projeto e acesse o diretório dele:

```sh
git clone https://github.com/DarkTechLC/docker-tutorial && cd docker-tutorial
```

- Inicie a aplicação:

```sh
docker-compose up -d
```

- No navegador, acesse [`http://localhost:8000`](http://localhost:8000).

- Para parar a aplicação:

```sh
docker-compose down
```
