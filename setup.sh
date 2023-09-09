#!/bin/bash

build(){
    docker compose build postgres pgadmin notebook tests
    docker build -t extending_airflow:latest -f ./docker/airflow/Dockerfile .
}

start(){
    docker compose up postgres pgadmin
    docker compose up airflow-init
    docker compose up postgres-airflow redis airflow-webserver airflow-scheduler airflow-worker flower
    docker compose up notebook
}

# the next line calls the function passed as the first parameter to the script.
# the remaining script arguments can be passed to this function.

$1