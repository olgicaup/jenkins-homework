pipeline {
    agent any

    environment {
        DOCKER_CREDENTIALS = 'dockerhub-creds' // Jenkins credentials ID for Docker Hub
        GITHUB_CREDENTIALS = 'github-creds'
    }

    stages {
        stage('Checkout') {
            steps {
                git credentialsId: "${GITHUB_CREDENTIALS}", url: 'https://github.com/olgicaup/jenkins-homework.git'
            }
        }
        stage('Build Docker Image') {
            steps {
                script {
                    sh 'docker build -t olgicaupcheva/jenkins-homework .'
                }
            }
        }
        stage('Push Docker Image') {
            steps {
                script {
                    withCredentials([usernamePassword(credentialsId: "${DOCKER_CREDENTIALS}", usernameVariable: 'DOCKER_USERNAME', passwordVariable: 'DOCKER_PASSWORD')]) {
                        sh 'echo $DOCKER_PASSWORD | docker login --username $DOCKER_USERNAME --password-stdin'
                    }
                    sh 'docker push olgicaupcheva/jenkins-homework'
                }
            }
        }
    }
}
