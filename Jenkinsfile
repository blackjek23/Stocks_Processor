pipeline {
    agent any

    environment {
        AWS_REGION = 'us-west-1'
        TF_IN_AUTOMATION = 'true'
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
                withAWS(credentials: 'aws-credentials-id', region: "${AWS_REGION}") {
                    sh 'terraform init'
                }
            }
        }

        stage('Terraform Apply') {
            steps {
                withAWS(credentials: 'aws-credentials-id', region: "${AWS_REGION}") {
                    sh 'terraform apply -auto-approve'
                }
            }
        }

        stage('terraform destroy') {
            steps {
                withAWS(credentials: 'aws-credentials-id', region: "${AWS_REGION}") {
                    sh 'terraform destroy -auto-approve'
                }
            }
        }
    }
}