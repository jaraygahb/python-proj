pipeline {
    agent any

    stages {
		stage('Build') {
            steps {
				catchError(buildResult: 'UNSTABLE', stageResult: 'FAILURE')
				{
					dir("testcases"){
						echo 'Testing success test case'
						bat 'C:/Users/Unique/AppData/Local/Programs/Python/Python39/python.exe -m unittest discover'
					}
				}
            }
        }
		stage('Publish Report') {
			steps {
				catchError(buildResult: 'UNSTABLE', stageResult: 'FAILURE')
				{
					dir("testcases"){
						echo 'Generating test case report'
						bat 'C:/Users/Unique/AppData/Local/Programs/Python/Python39/python.exe -m xmlrunner discover'
					}
				}
			}	
		}
		stage('Sonarqube') {
			environment {
			scannerHome = tool 'SonarQubeScanner'
			}
			steps {
				withSonarQubeEnv('sonarqube') {
				bat 'H:/sonar-scanner-cli-4.6.1.2450-windows/sonar-scanner-4.6.1.2450-windows/bin/sonar-scanner.bat'
				}
				timeout(time: 10, unit: 'MINUTES') {
				waitForQualityGate abortPipeline: true
				}
			}
		}
	}
	post {
    always {
      junit(
        allowEmptyResults: true,
        testResults: '**/testcases/*.xml'
      )
    }
	}
}