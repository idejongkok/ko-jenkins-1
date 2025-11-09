pipeline {
    agent any

    stages {
        stage('Run Python Script') {
            steps {
                sh '''
                docker exec python-runner bash -c "
                    python /app/test_api.py
                "
                '''
            }
        }
    }

    post {
        always {
            // optional: ambil report kalau script-nya generate file hasil (misal .html atau .log)
            sh '''
            docker cp python-runner:/app/reports ./reports || true
            '''
            archiveArtifacts artifacts: '**/reports/*', allowEmptyArchive: true
        }
    }
}
