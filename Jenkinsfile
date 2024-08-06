pipeline {
    agent any
    
    environment {
        AWS_REGION = 'us-west-1'
    }
    
    stages {
        stage('Deploy') {
            steps {
                withAWS(credentials: 'aws-credentials-id', region: "${AWS_REGION}") {
                    // Your AWS commands here
                    sh 'aws s3 ls'
                }
            }
        }
    }
}