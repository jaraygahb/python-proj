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