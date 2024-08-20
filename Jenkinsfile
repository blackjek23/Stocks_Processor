pipeline {
    agent any
    
    triggers{
        githubPush()
    }

    environment {
        AWS_REGION = 'us-west-1'
        TF_IN_AUTOMATION = 'true'
        AWS_CRED_FILE = 'secret.py'
        DOCKER_IMAGE_NAME_1 = 'blackjek23/downloader'
        DOCKER_IMAGE_NAME_2 = 'blackjek23/shreder'
    }


    stages {
        stage('Checkout') {
            steps {
                echo 'Pulling the repo from GitHub...'
                git 'https://github.com/blackjek23/Stocks_Processor.git' 
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
        withAWS(credentials: 'aws-credentials-id') {
                   sh """
                        echo "Access_key= '${AWS_ACCESS_KEY_ID}'" > ${AWS_CRED_FILE}
                        echo "Secret_access_key= '${AWS_SECRET_ACCESS_KEY}'" >> ${AWS_CRED_FILE}
                    """
                    sh "cat ${AWS_CRED_FILE}"
                }
            }
        }

        stage('Build Containers') {
            steps {
                
                    // Build your first Docker image
                    sh "cp ./secret.py ./downloader"
                    sh "docker build -t ${DOCKER_IMAGE_NAME_1}:1.${BUILD_NUMBER} ./downloader"
                    
                    // Build your second Docker image
                    sh "mv ./secret.py ./shreder"
                    sh "docker build -t ${DOCKER_IMAGE_NAME_2}:1.${BUILD_NUMBER} ./shreder"
                    
                    // Remove the temporary secret.py file
                    sh "rm ${AWS_CRED_FILE}"
                }
            }

        stage('Run Downloader Container') {
            steps {
                sh "docker run --rm ${DOCKER_IMAGE_NAME_1}:1.${BUILD_NUMBER}"
            }
        }

        stage('Run Shreder Container') {
            steps {
                sh "docker run --rm ${DOCKER_IMAGE_NAME_2}:1.${BUILD_NUMBER}"
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