# CI/CD Pipeline Example for python app

Example GitHub Actions workflow to build a Docker image, push it to Amazon ECR, and deploy it to Amazon EKS.

## Workflow Overview

1. **Build Docker Image:** This step builds a Docker image.

2. **Push to Amazon ECR:** This step pushed Docker image to Amazon ECR repository.

3. **Deploy to Amazon EKS:** This step deployed application to Amazon EKS cluster, use helm.

## Prerequisites

- Amazon EKS Cluster
- Amazon ECR Repository
- AWS IAM User with permissions to push to ECR and deploy to EKS (or .kubeconfig file located in github secrets)

## GitHub Secrets

Add the following secrets in your GitHub repository:

- `AWS_ACCESS_KEY_ID`: AWS IAM user access key ID
- `AWS_SECRET_ACCESS_KEY`: AWS IAM user secret access key
- `AWS_REGION`: AWS region

## Workflow Configuration

The GitHub Actions workflow is defined in the `.github/workflows/build-and-deploy.yml` file.
