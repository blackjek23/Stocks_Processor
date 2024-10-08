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
        // BUILD STARTS HERE !!!
        stage('build stage') {
            steps {
                // Checkout
                echo 'Pulling the repo from GitHub...'
                git 'https://github.com/blackjek23/Stocks_Processor.git' 

                // Credentials
                withAWS(credentials: 'aws-credentials-id') {
                   sh """
                        echo "Access_key= '${AWS_ACCESS_KEY_ID}'" > ${AWS_CRED_FILE}
                        echo "Secret_access_key= '${AWS_SECRET_ACCESS_KEY}'" >> ${AWS_CRED_FILE}
                    """    
                }
            }
        }

        // DEPLOY STARTS HERE !!!
        stage('deploy stage') {
            when {
                branch 'master'
            }
            steps {
            // Build your first Docker image
                sh "cp ./secret.py ./downloader"
                sh "docker build -t ${DOCKER_IMAGE_NAME_1}:1.${BUILD_NUMBER} ./downloader"
                
            // Build your second Docker image
                sh "mv ./secret.py ./shreder"
                sh "docker build -t ${DOCKER_IMAGE_NAME_2}:1.${BUILD_NUMBER} ./shreder"
            }
        }
        
        // CLEANUP STARTS HERE !!!    
        stage('cleaning stage') {
            when {
                branch 'master'
            }
            steps {
                // docker push to my dockerhub repo
                echo 'Uploading images and cleaning up...'
                sh "docker push ${DOCKER_IMAGE_NAME_1}:1.${BUILD_NUMBER}"
                sh "docker push ${DOCKER_IMAGE_NAME_2}:1.${BUILD_NUMBER}"
                sh '''
                docker rmi $(docker images -q) || true
                '''
            }
        }
    }
}