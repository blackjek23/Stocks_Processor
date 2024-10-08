pipeline {
    agent any
    
    triggers{
        githubPush()
    }

    environment {
        AWS_REGION = 'us-west-1'
        TF_IN_AUTOMATION = 'true'
        AWS_CRED_FILE = 'secret.py'
        DOCKER_REPO = 'blackjek23/'
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

                // Docekr build
                sh "cp ./secret.py ./$env.BRANCH_NAME"
                sh "docker build -t ${DOCKER_REPO}$env.BRANCH_NAME:1.${BUILD_NUMBER} ./$env.BRANCH_NAME"
            }
        }

        // TEST START HERE !!!
        stage('Test stage') {
            steps {
                script {
                    def exitCode = sh(script: "docker run ${DOCKER_REPO}$env.BRANCH_NAME:1.${BUILD_NUMBER}", returnStatus: true)
                    
                    if (exitCode == 0) {
                        echo "Container test passed"
                        currentBuild.result = 'SUCCESS'
                    } else {
                        echo "Container test failed with exit code: ${exitCode}"
                        error("Container test failed")
                    }
                }
            }
        }
    }

        // DEPLOY STARTS HERE !!!
        stage('deploy stage') {
            when {
                branch 'master' 
            }
            steps {
            // Build your worker Docker image 
                sh "cp ./secret.py .________"
                sh "docker build -t ${DOCKER_REPO}_______:1.${BUILD_NUMBER} ./_________"
            
            // Build your first Docker image
                sh "cp ./secret.py ./downloader"
                sh "docker build -t ${DOCKER_REPO}downloader:1.${BUILD_NUMBER} ./downloader"
                
            // Build your second Docker image
                sh "mv ./secret.py ./shreder"
                sh "docker build -t ${DOCKER_REPO}shreder:1.${BUILD_NUMBER} ./shreder"
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
                sh "docker push ${DOCKER_REPO}_________:1.${BUILD_NUMBER}"
                sh "docker push ${DOCKER_REPO}downloader:1.${BUILD_NUMBER}"
                sh "docker push ${DOCKER_REPO}shreder:1.${BUILD_NUMBER}"
                sh '''
                docker container prune -f
                docker rmi $(docker images -q) || true
                '''
            }
        }
    }
}




// name of the image ready for push'${DOCKER_REPO}$env.BRANCH_NAME:1.${BUILD_NUMBER}'