pipeline {
    agent any

    stages {
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
					bat 'C:/Users/Unique/AppData/Local/Programs/Python/Python39/python.exe -m unittest failure_testcase.py'
				}
            }
        }
		stage('Sucess Test Case') {
            steps {
                echo 'Testing success test case'
				bat 'C:/Users/Unique/AppData/Local/Programs/Python/Python39/python.exe -m unittest success_testcase.py'
				bat 'C:/Users/Unique/AppData/Local/Programs/Python/Python39/python.exe -m unittest success1_testcase.py'
            }
        }
    }
}