# Makefile for Terraform and Helm

# Terraform variables
TF_DIR := terraform

# Helm variables
HELM_DIR := helm-chart

# Terraform targets
init-terraform:
	@echo "Initializing Terraform..."
	cd $(TF_DIR) && terraform init

plan-terraform:
	@echo "Planning Terraform changes..."
	cd $(TF_DIR) && terraform plan

apply-terraform:
	@echo "Applying Terraform changes..."
	cd $(TF_DIR) && terraform apply

destroy-terraform:
	@echo "Destroying Terraform resources..."
	cd $(TF_DIR) && terraform destroy

# Helm targets
install-helm:
	@echo "Installing Helm charts..."
	cd $(HELM_DIR) && helm install --atomic python-simple-app --namespace=dev . --values dev.values.yaml

upgrade-helm:
	@echo "Upgrading Helm charts..."
	cd $(HELM_DIR) && helm upgrade --atomic python-simple-app --namespace=dev . --values dev.values.yaml

uninstall-helm:
	@echo "Uninstalling Helm charts..."
	cd $(HELM_DIR) && helm uninstall python-simple-app --namespace dev

.PHONY: init-terraform plan-terraform apply-terraform destroy-terraform install-helm upgrade-helm uninstall-helm
