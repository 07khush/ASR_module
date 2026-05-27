pipeline {
    agent any

    environment {
        IMAGE_NAME = 'khushi72003/whisper_model'
        TAG = 'latest'
    }

    stages {

        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                sh '''
                docker build -t $IMAGE_NAME:$TAG .
                '''
            }
        }

        stage('Push Docker Image') {
            steps {
                withCredentials([
                    usernamePassword(
                        credentialsId: 'dockerhub',
                        usernameVariable: 'USER',
                        passwordVariable: 'PASS'
                    )
                ]) {

                    sh '''
                    echo $PASS | docker login -u $USER --password-stdin
                    docker push $IMAGE_NAME:$TAG
                    '''
                }
            }
        }
    }

    post {
        success {
            echo 'Whisper ASR image pushed successfully'
        }

        failure {
            echo 'Pipeline failed'
        }

        always {
            sh 'docker logout || true'
        }
    }
}
