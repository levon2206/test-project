# Helm Chart for python application

## Overview

This Helm chart deploys python app to AWS EKS cluster
## Prerequisites

- AWS EKS cluster
- Helm installed ([Installation Guide](https://helm.sh/docs/intro/install/))

## Created K8s Resources
- Deployment
- HPA
- Service
- Service Accaunt 
- Service Monitor
- Extra Resources
- Ingress domain name - simple-app.example.com

Access to application 
 ```bash
 kubectl port-forward simple-app 5050:5050
 open localhost:5050
```

## Installation

Helm Values File name - ./helm-chart/dev.values.yaml
```bash
cd ./helm-chart

helm upgrade --install --atomic python-simple-app \
  --namespace=dev .chart \
  --values dev.values.yaml
```
### To Delete Chart

```bash
helm delete python-simple-app -n dev
