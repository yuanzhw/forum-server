#!/usr/bin/env bash
set -ex

apt update
apt install docker

docker build -t forum-server
docker network create forum-network
docker pull redis
docker run --name forum-server --network forum-network -d forum-server
docker run --name forum-redis --network forum-network -d redis