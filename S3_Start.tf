terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.0"
    }
  }
}

# Declare the variables
variable "aws_access_key" {
  description = "AWS Access Key"
  type        = string
}

variable "aws_secret_key" {
  description = "AWS Secret Key"
  type        = string
}

# Configure the AWS Provider
provider "aws" {
  access_key = var.aws_access_key
  secret_key = var.aws_secret_key
  region     = "us-west-1"  
}

# Create an S3 bucket
resource "aws_s3_bucket" "my_bucket" {
  bucket = "blackjek-bucket-unique"

  tags = {
    Name        = "My bucket"
    Environment = "Dev"
  }
}