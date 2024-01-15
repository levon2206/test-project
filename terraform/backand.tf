terraform {
  required_version = ">= 1.0.0"
  ## uncomment to enable terraform backand config, to save state file in remote provider
  backend "s3" {
    bucket         = "terraform-aws-eks-app"
    key            = "terraform.tfstate"
    region         = "eu-central-1"
    encrypt        = true
  }
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.0"
    }

  }
}

provider "kubernetes" {
  host                   = module.aws-eks.cluster_endpoint
  cluster_ca_certificate = base64decode(module.aws-eks.cluster_ca_certificate)
  token                  = data.aws_eks_cluster_auth.cluster.token
}
