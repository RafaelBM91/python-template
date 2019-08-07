pipeline {
    agent any
    stages {
        stage('Build') { 
            steps {
                sh 'make build'
            }
        }
        stage('Up') { 
            steps {
                sh 'make up'
            }
        }
    }
}
