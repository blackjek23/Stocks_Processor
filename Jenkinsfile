pipeline {

    agent any

    environment {
        AWS_REGION = 'us-west-1'
        TF_IN_AUTOMATION = 'true'
        AWS_CRED_FILE = 'secret.py'
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

         stage('Save AWS Credentials') {
            steps {
                credentials('aws-credentials-id') {
                    sh """
                        echo "AWS_ACCESS_KEY_ID=$AWS_ACCESS_KEY_ID" > ${AWS_CRED_FILE}
                        echo "AWS_SECRET_ACCESS_KEY=$AWS_SECRET_ACCESS_KEY" >> ${AWS_CRED_FILE}
                    """                }
            }
        }

        stage('terraform destroy') {
            steps {
                withAWS(credentials: 'aws-credentials-id', region: "${AWS_REGION}") {
                    sh 'terraform destroy -auto-approve'
                }
            }
        }

        stage('Verify AWS Credentials File') {
            steps {
                sh "cat ${AWS_CRED_FILE}"
            }
        }
    }
}