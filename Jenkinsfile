pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'git@github.com:idejongkok/ko-jenkins-1.git'
            }
        }

        stage('Setup Python Env') {
            steps {
                sh '''
                python3 -m venv venv
                source venv/bin/activate
                pip install -r requirements.txt
                '''
            }
        }

        stage('Run API Tests') {
            steps {
                sh '''
                source venv/bin/activate
                pytest --alluredir=api-automation/allure-results
                '''
            }
        }
        

        stage('Publish Allure Report') {
            steps {
                allure 'api-automation/allure-results'
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'api-automation/allure-results/**/*.*', fingerprint: true
        }
    }
}

