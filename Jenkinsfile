pipeline {
    agent any

    parameters {
        string(name: 'STUDENT_NAME', defaultValue: 'Nikhil Parab', description: 'Enter Student Name')
        string(name: 'STUDENT_USN', defaultValue: '01FE24BCA001', description: 'Enter Student USN')
        string(name: 'TOTAL_CLASSES', defaultValue: '40', description: 'Enter Total Number of Classes')
        string(name: 'ATTENDED_CLASSES', defaultValue: '35', description: 'Enter Number of Classes Attended')
    }

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

        stage('Run Attendance Checker') {
            steps {
                bat '(echo %STUDENT_NAME%& echo %STUDENT_USN%& echo %TOTAL_CLASSES%& echo %ATTENDED_CLASSES%) | "%DOCKER_EXE%" run --rm -i %IMAGE_NAME%'
            }
        }
    }

    post {
        always {
            bat '"%DOCKER_EXE%" image prune -f'
        }
        success {
            echo 'Attendance report generated successfully!'
        }
        failure {
            echo 'Pipeline failed during build or execution.'
        }
    }
}