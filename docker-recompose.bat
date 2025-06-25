@echo off

docker stop synpage
docker rm synpage

docker-compose pull
docker-compose up -d
docker-compose exec synpage /bin/bash