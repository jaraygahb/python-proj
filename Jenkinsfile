pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building..'
				sh "python ${WORKSPACE}/count.py"
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
            }
        }
    }
}