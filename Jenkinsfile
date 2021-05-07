pipeline {
    agent any

    stages {
		stage('CleanWorkspace') {
            steps {
                cleanWs()
            }
		}
	
        stage('Build') {
            steps {
                echo 'Building..'
				bat 'C:/Users/Unique/AppData/Local/Programs/Python/Python39/python.exe count.py'
            }
        }
		stage('Failure Test Case') {
            steps {
				catchError(buildResult: 'SUCCESS', stageResult: 'FAILURE')
				{
					echo 'Testing failure test case'
					bat 'C:/Users/Unique/AppData/Local/Programs/Python/Python39/python.exe -m unittest testcases/failure_testcase.py'
				}
            }
        }
		stage('Sucess Test Case') {
            steps {
                echo 'Testing success test case'
				bat 'C:/Users/Unique/AppData/Local/Programs/Python/Python39/python.exe -m unittest testcases/success_testcase.py'
				bat 'C:/Users/Unique/AppData/Local/Programs/Python/Python39/python.exe -m unittest testcases/success1_testcase.py'
            }
        }
		stage('Report') {
			steps {
				catchError(buildResult: 'SUCCESS', stageResult: 'FAILURE') {
					echo 'Generating test case report'
					bat 'C:/Users/Unique/AppData/Local/Programs/Python/Python39/python.exe -m pytest --junit-xml=result.xml testcases/alltests.py'
					step([$class: 'ACIPluginPublisher', name: '*.xml', shownOnProjectPage: true])
				}
			}
		}
    }
}