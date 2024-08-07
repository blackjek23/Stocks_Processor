pipeline {
    agent any

    environment {
        AWS_REGION = 'us-west-1'
        TF_IN_AUTOMATION = 'true'
        AWS_ACCESS_KEY_ID = credentials('aws-credentials-id')
        AWS_SECRET_ACCESS_KEY = credentials('aws-credentials-id')
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

        stage('Build Container 1') {
            steps {
                dir('downloader') {
                    script {
                        def secretFile = 'secret.py'
                        writeFile file: secretFile, text: """
AWS_ACCESS_KEY_ID = '${AWS_ACCESS_KEY_ID}'
AWS_SECRET_ACCESS_KEY = '${AWS_SECRET_ACCESS_KEY}'
"""
                        sh 'docker build -t container1 .'
                    }
                }
            }
        }

        stage('Build Container 2') {
            steps {
                dir('shreder') {
                    script {
                        def secretFile = 'secret.py'
                        writeFile file: secretFile, text: """
AWS_ACCESS_KEY_ID = '${AWS_ACCESS_KEY_ID}'
AWS_SECRET_ACCESS_KEY = '${AWS_SECRET_ACCESS_KEY}'
"""
                        sh 'docker build -t container2 .'
                    }
                }
            }
        }

        stage('Run Container 1') {
            steps {
                script {
                    sh 'docker run --rm container1'
                }
            }
        }

        stage('Run Container 2') {
            steps {
                script {
                    sh 'docker run --rm container2'
                }
            }
        }
    }
}