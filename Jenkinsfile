pipeline {
    agent any
    
    triggers{
        githubPush()
    }

    environment {
        AWS_CREDENTIALS = credentials('aws-credentials-id') 
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

        stage('Terraform Apply') {
            steps {
                echo 'Running Terraform with AWS credentials...'
                withCredentials([[
                    $class: 'AmazonWebServicesCredentialsBinding',
                    credentialsId: 'aws-credentials-id',  
                    accessKeyVariable: 'AWS_ACCESS_KEY_ID',
                    secretKeyVariable: 'AWS_SECRET_ACCESS_KEY'
                ]]) {
                    sh 'terraform init'
                    sh 'terraform apply -auto-approve'
                }
            }
        }

        stage('Build Containers') {
            steps {
                echo 'Building containers with AWS credentials...'
                script {
                    def awsAccessKey = env.AWS_ACCESS_KEY_ID
                    def awsSecretKey = env.AWS_SECRET_ACCESS_KEY
                    
                    // Create a temporary secret.py file with AWS credentials
                    sh """
                    echo "AWS_ACCESS_KEY = '${awsAccessKey}'" > secret.py
                    echo "AWS_SECRET_KEY = '${awsSecretKey}'" >> secret.py
                    echo "region_name = 'us-west-1' " >>> secret.py
                    """
                    
                    // Build your first Docker image
                    sh "docker build -t ${DOCKER_IMAGE_NAME_1}:1.${BUILD_NUMBER} ./downloader"
                    
                    // Build your second Docker image
                    sh "docker build -t ${DOCKER_IMAGE_NAME_2}:1.${BUILD_NUMBER} ./shreder"
                    
                    // Remove the temporary secret.py file
                    sh 'rm secret.py'
                }
            }
        }

        stage('Run First Container') {
            steps {
                echo 'Running the first container...'
                script {
                    def containerId = sh(script: "docker run -d ${DOCKER_IMAGE_NAME_1}:1.${BUILD_NUMBER}", returnStdout: true).trim()
                    echo "First container ID: ${containerId}"

                    // Wait for the container to finish
                    sh "docker wait ${containerId}"
                    
                    // Check the exit code
                    def exitCode = sh(script: "docker inspect ${containerId} --format='{{.State.ExitCode}}'", returnStdout: true).trim()
                    echo "First container exited with code: ${exitCode}"

                    if (exitCode != "0") {
                        error "First container failed with exit code ${exitCode}"
                    }
                }
            }
        }

        stage('Run Second Container') {
            steps {
                echo 'Running the second container...'
                sh "docker run -d ${DOCKER_IMAGE_NAME_2}:1.${BUILD_NUMBER}"
            }
        }
    }

    post {
        always {
            echo 'Cleaning up...'
            sh 'docker rm $(docker ps -a -q)' 
        }
    }
}