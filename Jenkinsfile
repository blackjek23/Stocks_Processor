pipeline {
    agent any

    environment {
        AWS_CREDENTIALS = credentials('aws-credentials-id')  // Replace with your actual credentials ID
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
                withCredentials([[
                    $class: 'AmazonWebServicesCredentialsBinding',
                    credentialsId: 'aws-credentials-id',  // Replace with your actual credentials ID
                    accessKeyVariable: 'AWS_ACCESS_KEY_ID',
                    secretKeyVariable: 'AWS_SECRET_ACCESS_KEY'
                ]]) {
                    sh 'terraform init'
                }
            }
        }

        stage('Terraform Apply') {
            steps {
                echo 'Applying Terraform changes'
                withCredentials([[
                    $class: 'AmazonWebServicesCredentialsBinding',
                    credentialsId: 'aws-credentials-id',  // Replace with your actual credentials ID
                    accessKeyVariable: 'AWS_ACCESS_KEY_ID',
                    secretKeyVariable: 'AWS_SECRET_ACCESS_KEY'
                ]]) {
                    sh '''
                    terraform apply -auto-approve \
                    -var="aws_access_key=$AWS_ACCESS_KEY_ID" \
                    -var="aws_secret_key=$AWS_SECRET_ACCESS_KEY"
                    '''
                }
            }
        }
    }
}