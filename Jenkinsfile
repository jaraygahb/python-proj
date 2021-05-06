pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building..'
				bat 'python ./count.py'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
            }
        }
    }
}