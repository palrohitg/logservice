#!/bin/bash

docker network create my-network
# Run docker-compose with your desired options
docker-compose -f docker-compose.yml up --build 