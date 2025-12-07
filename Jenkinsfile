pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps { checkout scm }
        }

        stage('Build Image for Testing') {
            steps {
                // Собираем образ, чтобы прогнать тесты внутри
                sh 'docker build -t test-image .'
            }
        }

        stage('Run Unit Tests') {
            steps {
                // Запускаем pytest внутри контейнера
                // Если тесты упадут, пайплайн остановится и Deploy не начнется
                sh 'docker run --rm test-image pytest'
            }
        }

        stage('Deploy') {
            steps {
                // Этот шаг выполнится ТОЛЬКО если тесты прошли
                sh 'docker-compose up -d --build'
            }
        }
    }
}