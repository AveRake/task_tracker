pipeline {
    agent any

    environment {
        COMPOSE_PROJECT_NAME = "tasktracker_deploy"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Create .env File') {
            steps {
                script {
                    sh """
                        echo "POSTGRES_USER=myuser" > .env
                        echo "POSTGRES_PASSWORD=mypassword" >> .env
                        echo "POSTGRES_DB=taskdb" >> .env
                    """
                }
            }
        }

        stage('Build Image for Testing') {
            steps {
                sh 'docker build -t test-image .'
            }
        }

        stage('Run Unit Tests') {
            steps {
                sh 'docker run --rm test-image pytest'
            }
        }

        stage('Deploy') {
            steps {
                script {
                    sh 'docker-compose down'
                    sh 'docker-compose up -d --build'
                }
            }
        }
    }
}