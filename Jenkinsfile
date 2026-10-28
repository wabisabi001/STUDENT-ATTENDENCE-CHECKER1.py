pipeline {
    agent any

    environment {
        IMAGE_NAME = "student-attendance:latest"
        DOCKER_EXE = "C:\\Users\\nikhi\\AppData\\Local\\Programs\\DockerDesktop\\resources\\bin\\docker.exe"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                bat '"%DOCKER_EXE%" build -t %IMAGE_NAME% .'
            }
        }

        stage('Test Execution') {
            steps {
                bat '(echo John Doe& echo 1CR21CS001& echo 40& echo 32) | "%DOCKER_EXE%" run --rm -i %IMAGE_NAME%'
            }
        }
    }

    post {
        always {
            bat '"%DOCKER_EXE%" image prune -f'
        }
        success {
            echo 'Build, packaging, and execution completed successfully!'
        }
        failure {
            echo 'Pipeline failed during build or execution.'
        }
    }
}