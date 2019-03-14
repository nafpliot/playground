#!/usr/bin/env bash

if ! minikube status > /dev/null 2>&1; then
    echo "Please start minikube"
    exit 1
fi

eval $(minikube docker-env)
docker build -t server:latest server/
docker build -t collector:latest collector/
kubectl create -f k8s_deployment/server.yml
kubectl create -f k8s_deployment/collector.yml