pipeline {
    agent any

    environment {
        IMAGE_NAME = "myapp"
        IMAGE_TAG  = "latest"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh "docker build -t ${IMAGE_NAME}:${IMAGE_TAG} ."
                }
            }
        }

        stage('Run Container') {
            steps {
                script {
                    // Stop and remove any old container
                    sh """
                        docker ps -q --filter "name=${IMAGE_NAME}" | grep -q . && docker stop ${IMAGE_NAME} && docker rm ${IMAGE_NAME} || true
                        docker run -d --name ${IMAGE_NAME} -p 5000:5000 ${IMAGE_NAME}:${IMAGE_TAG}
                    """
                }
            }
        }
    }
}
