pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building..'
				bat 'count.py'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
            }
        }
    }
}