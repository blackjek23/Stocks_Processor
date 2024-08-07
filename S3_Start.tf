terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.0"
    }
  }
}

# Configure the AWS Provider
provider "aws" {
  region = "us-west-1"  
  # Remove the access_key and secret_key here
  # Terraform will use the AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY 
  # environment variables set by Jenkins
}

# Create an S3 bucket
resource "aws_s3_bucket" "my_bucket" {
  bucket = "blackjek-bucket-unique"

  tags = {
    Name        = "My bucket"
    Environment = "Dev"
  }
}