# Containerized Microservice

This example demonstrates two Flask applications running in docker containers, deployed on Kubernetes (minikube).

The first app (server) exposes a json document on port 5000 which includes a message and the pod name where the container runs, while the second (collector) reads this json and reverses the message.

The deployment files create one pod for each app with 1 replica + the services.

An easy way to run the environment is to use the `deploy.sh` script.

## Extra Info

The deployments are configured for rolling updates, using `RollingUpdate` strategy and a `readinessProbe`.
To try it out we can increase the replicas with `kubectl scale deployments/server --replicas=2` and then set the new docker image `kubectl set image deployments/server server=server:foo`