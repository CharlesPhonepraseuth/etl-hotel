#!/bin/bash

stop(){
    docker compose down
}

cleanup(){
    docker compose down

    docker rm -f $(docker ps -a -q)
    docker image rm $(docker image ls -q)
    docker volume rm $(docker volume ls -q)
    docker network rm $(docker network ls -q)

    docker image ls
    docker volume ls
    docker container ls
    docker network ls
}

# the next line calls the function passed as the first parameter to the script.
# the remaining script arguments can be passed to this function.

$1