pipeline {
    agent any

    environment {
        AWS_REGION = 'us-west-1'
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
                {
                    sh 'terraform init'
                }
            }
        }

        stage('Terraform Apply') {
            steps {
                echo 'Applying Terraform changes'
                withAWS(credentials: 'aws-credentials-id', region: "${AWS_REGION}") {
                }
                {
                    sh '''
                    terraform apply -auto-approve
                    '''
                }
            }
        }

        stages {
        stage('Deploy') {
            
                }
            }
        }
    }

    