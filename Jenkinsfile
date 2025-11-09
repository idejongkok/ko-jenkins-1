pipeline {
    agent any

    stages {
        stage('Install Dependencies') {
            steps {
                sh '''
                docker exec python-runner bash -c "
                    cd '/var/jenkins_home/workspace/API_Test' &&
                    pip install -r requirements.txt
                "
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                docker exec python-runner bash -c "
                    cd '/var/jenkins_home/workspace/API_Test' &&
                    pytest -v
                "
                '''
            }
        }
    }
}

