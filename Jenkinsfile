pipeline {
    agent any

    environment {
        VENV_DIR = 'venv'
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'master', url: 'git@github.com:idejongkok/ko-jenkins-1.git'
            }
        }

        stage('Setup Python Env') {
            steps {
                sh '''
                python3 -m venv ${VENV_DIR}
                . ${VENV_DIR}/bin/activate
                python -m pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }

        stage('Run API Tests') {
            steps {
                sh '''
                . ${VENV_DIR}/bin/activate
                pytest api-automation/tests --alluredir=api-automation/allure-results
                '''
            }
        }

        stage('Publish Allure Report') {
            steps {
                script {
                    allure([
                        includeProperties: false,
                        jdk: '',
                        results: [[path: 'api-automation/allure-results']]
                    ])
                }
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'api-automation/allure-results/**/*.*', fingerprint: true
            junit 'api-automation/allure-results/**/*.xml'
        }
        cleanup {
            sh 'rm -rf ${VENV_DIR}'
        }
    }
}
