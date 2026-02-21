# Terraform-Deployed Dockerized Flask Application on AWS

## Overview
This project demonstrates the end-to-end deployment of a containerized web application on AWS using Infrastructure as Code (IaC). A lightweight Flask application is packaged with Docker and deployed to an EC2 instance provisioned via Terraform, showcasing core cloud engineering and DevOps fundamentals.

The repository is designed to reflect professional best practices, including reproducible infrastructure, artifact exclusion, and source-controlled configuration.

## Purpose
This project is intended as a learning and portfolio artifact to demonstrate foundational skills in cloud infrastructure, containerization, and DevOps workflows.

---

## Architecture
- **Application:** Python Flask web application
- **Containerization:** Docker
- **Cloud Provider:** AWS
- **Compute:** EC2 (Free Tier eligible instance)
- **Infrastructure as Code:** Terraform
- **Version Control:** Git + GitHub

High-level flow:
1. Flask app is containerized using Docker
2. Terraform provisions AWS infrastructure (EC2, networking, security groups)
3. EC2 user data installs Docker and runs the application container
4. Application is exposed via EC2 public IP and port mapping

---

## Repository Structure
├── app/
│ └── app.py
├── terraform/
│ ├── main.tf
│ ├── variables.tf
│ └── outputs.tf
├── Dockerfile
├── requirements.txt
├── .gitignore
└── README.md

---

## Key Features
- Dockerized Flask application for consistent runtime behavior
- Terraform-managed AWS infrastructure (reproducible and declarative)
- Secure networking via AWS security groups
- Automated instance bootstrapping using EC2 user data
- Clean Git history with generated artifacts excluded

---

## Prerequisites
- AWS account (Free Tier)
- Terraform installed locally
- Docker installed locally
- AWS credentials configured (`aws configure`)
- Git

---

## Deployment Steps

### 1. Build and Push Docker Image
docker build -t <docker-username>/flask-app .
docker push <docker-username>/flask-app

### 2. Initialize and Apply Terraform
cd terraform
terraform init
terraform apply

Terraform will output the EC2 public IP once provisioning is complete.

### Infrastructure and DevOps Best Practices
 - Terraform provider binaries and state files are excluded from version control
 - Python virtual environments are not committed
 - Infrastructure changes are validated using terraform plan
 - Application artifacts are rebuilt deterministically

### Limitations
 - Single EC2 instance (no load balancing or auto-scaling)
 - Stateless application
 - No CI/CD pipeline implemented (intentionally scoped)

### Future Improvements
 - Add remote Terraform state (S3 + DynamoDB)
 - Introduce CI/CD with GitHub Actions
 - Migrate to ECS or EKS
 - Add observability (CloudWatch logs and metrics)
 - Persist state using a managed database
