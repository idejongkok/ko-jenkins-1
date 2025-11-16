pipeline {
    agent any

    stages {
        stage('Setup Python Env') {
            steps {
                sh '''
                docker exec python-runner bash -c "
                    python3 -m venv /app/venv && \
                    . /app/venv/bin/activate && \
                    pip install -r /app/requirements.txt
                "
                '''
            }
        }

        stage('Run API Tests') {
            steps {
                sh '''
                docker exec python-runner bash -c "
                    . /app/venv/bin/activate && \
                    pytest --maxfail=1 --disable-warnings -q --html=/app/reports/report.html
                "
                '''
            }
        }
    }

    post {
        always {
            sh 'docker cp python-runner:/app/reports ./reports || true'
            archiveArtifacts artifacts: 'reports/*.html', allowEmptyArchive: true
        }
    }
}
