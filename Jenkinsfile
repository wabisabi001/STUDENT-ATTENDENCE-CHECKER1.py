pipeline {
    agent any

    environment {
        IMAGE_NAME = "student-attendance:latest"
        PATH = "C:\\Program Files\\Docker\\Docker\\resources\\bin;${env.PATH}"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t %IMAGE_NAME% .'
            }
        }

        stage('Test Execution') {
            steps {
                bat '(echo John Doe& echo 1CR21CS001& echo 40& echo 32) | docker run --rm -i %IMAGE_NAME%'
            }
        }
    }

    post {
        always {
            bat 'docker image prune -f'
        }
        success {
            echo 'Build, packaging, and execution completed successfully!'
        }
        failure {
            echo 'Pipeline failed during build or execution.'
        }
    }
}