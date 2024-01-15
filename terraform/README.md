# Terrafrom AWS EKS-VPC-ECR module

Terraform module to create ASW EKS, VPC and ECR Resources

## Prerequisites

List of prerequisites

- [Terraform](https://www.terraform.io/downloads.html) version >= v1.5.7
- AWS CLI installed and configured with appropriate credentials

## Getting Started
- Setup AWS EKS cluster and VPC
- Install ebs-csi-driver-controller
- Setup ECR repository

## Created Resources

AWS EKS cluster
 - k8s version - 1.28
 - Ebs_csi_driver_controller version - v1.25.0
 - 1 node - t3.small type
 - Public access with nat gateway

AWS VPC 
 - Availability zones - us-west-1a, us-west-1b
 - VPC cidrblock block - 172.30.0.0/16
 - Public subnets ip range - 172.30.32.0/20, 172.30.16.0/20, 172.30.0.0/20
 - Private subnets ip range - 172.30.48.0/20, 172.30.64.0/20, 172.30.80.0/20
 - Nat gateway
 - Internet gateway
 - Route tables

AWS ECR repository

- ECR repository name - simple-app
  
### Installation

Usage commands.

```bash
# Clone the repository
git clone https://github.com/naviteq/lab-work-levon-ananyan.git

# Change into the project directory
cd ./terraform

# Configure AWS CLI with your credentials
aws configure

# Initialize Terraform
terraform init

# Plan and apply changes
terraform plan
terraform apply

# Plan to Destroy
terraform destroy

⚠️ **IMPORTANT**    
For Production Usage configure terraform remote state in AWS S3 or other providers
(https://developer.hashicorp.com/terraform/language/settings/backends/s3)
```
```
Directory Structure

├── main.tf
├── variables.tf
├── backand.tf
├── data.tf
├── outputs.tf
│   ├── aws-ecr/
│   │   ├── main.tf
│   │   ├── variables.tf
│   │   ├── outputs.tf
│   ├── aws-eks/
│   │   ├── main.tf
│   │   ├── variables.tf
│   │   ├── outputs.tf
│   ├── aws-vpc/
│   │   ├── main.tf
│   │   ├── variables.tf
│   │   ├── outputs.tf
└── ...
