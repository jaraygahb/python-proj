pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building..'
				bat 'C:/Users/Unique/AppData/Local/Programs/Python/Python39/python.exe count.py'
            }
        }
		stage('Sucess Test Case') {
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
		stage('Report') {
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