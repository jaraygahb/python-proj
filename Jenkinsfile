pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building..'
				sh 'python count.py'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
            }
        }
    }
}