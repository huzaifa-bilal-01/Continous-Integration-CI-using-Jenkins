pipeline {
    agent any

    environment {
        DOCKER_IMAGE_NAME = 'usman0416/mlops-assignment-1:latest'
    }

    stages {
        stage('Build Docker Image') {
            steps {
                script {
                    // Build the Docker image
                    bat "docker build -t $DOCKER_IMAGE_NAME ."
                }
            }
        }

        stage('Login Dockerhub abd Push Docker Image') {
            environment {
                DOCKER_HUB_CREDENTIALS = credentials('dockerhub-credentials')
            }
            steps {
                script {
                    // Log in to Docker Hub securely
                    withCredentials([usernamePassword(credentialsId: 'dockerhub-credentials', usernameVariable: 'DOCKER_HUB_USERNAME', passwordVariable: 'DOCKER_HUB_PASSWORD')]) {
                        bat "echo $DOCKER_HUB_PASSWORD | docker login -u $DOCKER_HUB_USERNAME --password-stdin"

                        // Push the Docker image to Docker Hub
                        bat "docker push $DOCKER_IMAGE_NAME"
                    }
                }
            }
        }
    }

    post {
        always {
            // Clean up Docker images
            sh 'docker system prune -af'
        }
        success {
            echo 'Pipeline Success'
            // Sending an email notification with details about the success
            mail bcc: '', body: "<br>Project: ${env.JOB_NAME} <br>Build Number: ${env.BUILD_NUMBER} <br> URL de build: ${env.BUILD_URL}", cc: '', charset: 'UTF-8', from: '', mimeType: 'text/html', replyTo: '', subject: "Success CI: Project name -> ${env.JOB_NAME}", to: "usmanamir2580@gmail.com";
        }
        failure {
            echo 'Pipeline Failed'
            // Sending an email notification with details about the failure
            mail bcc: '', body: "<br>Project: ${env.JOB_NAME} <br>Build Number: ${env.BUILD_NUMBER} <br> URL de build: ${env.BUILD_URL}", cc: '', charset: 'UTF-8', from: '', mimeType: 'text/html', replyTo: '', subject: "ERROR CI: Project name -> ${env.JOB_NAME}", to: "usmanamir2580@gmail.com";
        }
    }
}