#!/usr/bin/env groovy
pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh 'docker build -t tornado_web:latest .'
            }
        }
        stage('Test') {
            steps {
                sh 'docker-compose up'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}