pipeline {
    agent any

    environment {
        AWS_CREDENTIALS = credentials('aws-credentials-id')  // Replace with your actual credentials ID
        TF_VAR_aws_access_key = credentials('aws-credentials-id').accessKey
        TF_VAR_aws_secret_key = credentials('aws-credentials-id').secretKey
    }

    stages {
        stage('Fetch Repository') {
            steps {
                echo 'Fetching git repository'
                git url: 'https://github.com/blackjek23/Stocks_Processor.git'
            }
        }
        
        stage('Terraform Init') {
            steps {
                echo 'Initializing Terraform'
                sh 'terraform init'
            }
        }

        stage('Terraform Apply') {
            steps {
                echo 'Applying Terraform changes'
                sh 'terraform apply -auto-approve'
            }
        }
    }
}