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

# using claude