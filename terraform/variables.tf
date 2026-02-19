variable "aws_region" {
  default = "us-west-1"
}

# variable "key_name" {
#   description = "EC2 key pair name"
# }

variable "docker_image" {
  description = "Docker Hub image (e.g. username/flask-app:latest)"
  default = "doejon/cloud_project"
}
