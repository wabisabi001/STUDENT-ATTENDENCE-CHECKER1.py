pipeline {
    agent any

    environment {
        IMAGE_NAME = "student-attendance:latest"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t ${IMAGE_NAME} .'
            }
        }

        stage('Test Execution') {
            steps {
                // Feeds sample input (Name, USN, Total Classes, Attended Classes) non-interactively
                sh '''
                    printf "John Doe\\n1CR21CS001\\n40\\n32\\n" | docker run --rm -i ${IMAGE_NAME}
                '''
            }
        }
    }

    post {
        always {
            // Remove test container remnants
            sh 'docker image prune -f || true'
        }
        success {
            echo 'Build, packaging, and execution completed successfully!'
        }
        failure {
            echo 'Pipeline failed during build or execution.'
        }
    }
}