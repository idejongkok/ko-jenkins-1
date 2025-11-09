pipeline {
    agent any

    stages {
        stage('Install Dependencies') {
            steps {
                sh '''
                docker exec python-runner bash -c "
                    pip install -r /app/requirements.txt
                "
                '''
            }
        }

        stage('Run API Tests') {
            steps {
                sh '''
                docker exec python-runner bash -c "
                    pytest --maxfail=1 --disable-warnings -q --html=/app/reports/report.html
                "
                '''
            }
        }
    }

    post {
        always {
            // copy hasil laporan dari container ke Jenkins workspace
            sh '''
            docker cp python-runner:/app/reports ./reports || true
            '''
            archiveArtifacts artifacts: '**/reports/*.html', allowEmptyArchive: true
        }
    }
}
