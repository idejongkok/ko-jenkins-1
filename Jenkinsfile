pipeline {
    agent {
        docker {
            image 'python:3.11'
            args '-v /var/run/docker.sock:/var/run/docker.sock'
        }
    }

    environment {
        ALLURE_RESULTS = 'allure-results'
        ALLURE_REPORT = 'allure-report'
    }

    stages {
        stage('Checkout') {
            steps {
                dir('api-automation') {
                    git branch: 'master', url: 'https://github.com/username/api-automation.git'
                }
            }
        }

        stage('Install Dependencies') {
            steps {
                dir('api-automation') {
                    sh '''
                    pip install --upgrade pip
                    pip install -r requirements.txt
                    '''
                }
            }
        }

        stage('Run Tests') {
            steps {
                dir('api-automation') {
                    sh '''
                    pytest --alluredir=$ALLURE_RESULTS
                    '''
                }
            }
        }

        stage('Generate Allure Report') {
            steps {
                dir('api-automation') {
                    sh '''
                    apt-get update && apt-get install -y unzip curl
                    curl -o allure.zip -L https://github.com/allure-framework/allure2/releases/latest/download/allure-2.29.0.zip
                    unzip allure.zip -d /opt/
                    ln -s /opt/allure-2.29.0/bin/allure /usr/bin/allure
                    allure generate $ALLURE_RESULTS -o $ALLURE_REPORT --clean
                    '''
                }
            }
        }

        stage('Publish Allure Report') {
            steps {
                allure includeProperties: false, jdk: '', results: [[path: 'api-automation/allure-results']]
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'api-automation/allure-results/**', allowEmptyArchive: true
        }
        failure {
            echo "Weh testnya gagal — Check Allure Report in Jenkins."
        }
        success {
            echo "Semua test passed!"
        }
    }
}
