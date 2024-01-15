# Simple python app Flux v2 Application

## Introduction

This repository contains the configuration for deploying and managing my application using Flux v2. Flux is a GitOps tool that helps automate the deployment and lifecycle management of Kubernetes resources.

## Installation

1. Install Flux CLI:

   ```bash
   curl -s https://toolkit.fluxcd.io/install.sh | sudo bash

## Install Flux in cluster:

flux bootstrap github \
  --owner=<your-github-username> \
  --repository=my-flux-repo \
  --branch=main \
  --path=/fluxv2

## Flux Usage/Examples

1. Deploy and update infrastracture components (monitoring, logging and etc) - /releases/infra
2. Automate image updates - releases/app
