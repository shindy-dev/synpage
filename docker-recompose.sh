#!/bin/bash

docker stop synpage || true && docker rm synpage || true && docker-compose up -d && docker-compose exec synpage /bin/bash