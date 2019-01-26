pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building docker image'
                docker build -t tornado_web:latest .
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}