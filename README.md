# Cloud-Native Flask Application

A cloud-native web application built with **Python**, **Flask**, **Docker**, **Terraform**, **AWS**, and **Kubernetes** to demonstrate modern Cloud Engineering and DevOps practices. The project emphasizes Infrastructure as Code, containerization, Kubernetes orchestration, and reproducible deployments.

---

## Project Overview

This project began as a simple Flask web application and evolved into a cloud-native deployment platform.

Key goals included:

* Containerizing applications with Docker
* Automating infrastructure using Terraform
* Deploying workloads to Kubernetes
* Managing configuration through ConfigMaps
* Implementing Kubernetes health checks
* Demonstrating scalable, reproducible deployments
* Following Infrastructure as Code (IaC) best practices

---

## Architecture

```text
                        GitHub Repository
                               │
                               ▼
                     Docker Image Build
                               │
                               ▼
                         Docker Hub Registry
                               │
                               ▼
                   Kubernetes Deployment
                               │
            ┌──────────────────┴──────────────────┐
            ▼                                     ▼
        Flask Pod                           Flask Pod
            │                                     │
            └──────────────┬──────────────────────┘
                           ▼
                   Kubernetes Service
                           │
                           ▼
                        Application
```

---

## Technology Stack

### Cloud

* AWS
* Terraform

### Containerization

* Docker
* Docker Hub

### Container Orchestration

* Kubernetes (Kind)

### Backend

* Python
* Flask

### DevOps

* Git
* GitHub

---

## Features

### Application

* Python Flask web application
* Dockerized runtime
* Environment-based configuration
* Health endpoint

### Infrastructure

* Infrastructure as Code with Terraform
* Version-controlled infrastructure
* Automated cloud resource provisioning

### Kubernetes

* Deployment resources
* Service resources
* ConfigMaps
* Readiness probes
* Liveness probes
* Replica management

### Source Control

* Git-based workflow
* Optimized `.gitignore`
* Clean repository structure
* Excluded Terraform state and generated artifacts

---

## Repository Structure

```text
.
├── app.py
├── requirements.txt
│
├── k8s/
│   ├── deployment.yaml
│   ├── service.yaml
│   ├── configmap.yaml
│
├── terraform/
│   ├── main.tf
│   ├── variables.tf
│   ├── outputs.tf
|   ├── ec2.tf
│   └── providers.tf
│
├── .dockerignore
├── .gitignore
└── README.md
```

---

## Kubernetes Components

### Deployment

* Deploys multiple replicas of the Flask application
* Supports rolling updates
* Enables horizontal scaling

### Service

* Provides a stable endpoint for accessing the application
* Performs service discovery and load balancing

### ConfigMap

Application configuration is managed outside of source code.

Example:

```yaml
APP_ENV: kubernetes
```

### Readiness Probe

Determines when a Pod is ready to receive traffic.

Validated by intentionally failing the health endpoint and confirming Kubernetes removed the Pod from Service endpoints.

### Liveness Probe

Determines whether Kubernetes should restart a failed container.

Validated by forcing health check failures and observing Kubernetes automatically recover the workload.

---

## Infrastructure as Code

Terraform provisions cloud infrastructure using declarative configuration.

Current infrastructure includes:

* AWS compute resources
* Networking configuration
* Security configuration
* Version-controlled infrastructure definitions

---

## Docker

The application is packaged into a lightweight Docker image using a multi-step, reproducible build process.

Improvements made during development:

* Added `.dockerignore`
* Removed unnecessary build artifacts
* Optimized image size
* Published images to Docker Hub

---

## Lessons Learned

Throughout development, several real-world engineering challenges were encountered and resolved:

* Optimizing oversized Docker images
* Managing Git repository history and large generated files
* Excluding Terraform state from version control
* Debugging Kubernetes deployments
* Validating readiness and liveness probes
* Separating application configuration using ConfigMaps
* Troubleshooting container networking and deployment issues

## Future Improvements

* GitHub Actions CI/CD pipeline
* Deploy to Amazon EKS
* Helm chart packaging
* Prometheus monitoring
* Grafana dashboards
* Centralized logging
* PostgreSQL persistence
* Secrets management
* Horizontal Pod Autoscaler
* Ingress controller
* TLS/HTTPS
* Automated testing
* Blue/Green or Canary deployments
