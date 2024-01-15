# CI/CD Pipeline example to create infra and deploy app to aws eks.

GitLab CI/CD pipelines to create infrastracture, build a Docker image, push it to Amazon ECR, and deploy it to Amazon EKS.

## Pipeline Overview

1. **./gitlab/infra.gitlab-ci.yml** Create AWS EKS, VPC and ECR use terraform.

2. **./gitlab/app.gitlab-ci.yml/build:** Build image and push to ECR.

3. **./gitlab/app.gitlab-ci.yml/deploy** Deploy image to eks use helm chart.

## Prerequisites

- Amazon EKS Cluster
- Amazon ECR Repository
- AWS IAM User with permissions to push to ECR and deploy to EKS

## GitLab CI/CD Configuration

The GitLab CI/CD pipeline is defined in the `.gitlab-ci.yml` file. 
1) .gitlab/infra.gitlab-ci.yml - deploy and destroy infrastracture.
2) .gitlab/app.gitlab-ci.yml - build and deploy app in EKS

⚠️ **IMPORTANT**    
Save youre terraform state file in gitlab
