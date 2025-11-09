pipeline {
    agent any

    environment {
        CONTAINER_NAME = 'python-runner'
        APP_PATH = '/app'
    }

    stages {
        stage('Debug Workspace') {
            steps {
                sh '''
                echo "Current Jenkins workspace:"
                pwd
                echo "List workspace contents:"
                ls -al
                '''
            }
        }

        stage('Copy Files to Container') {
            steps {
                sh '''
                echo "Copying repository files into container..."
                docker cp . ${CONTAINER_NAME}:${APP_PATH}
                docker exec ${CONTAINER_NAME} bash -c "ls -al ${APP_PATH}"
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                docker exec ${CONTAINER_NAME} bash -c "
                    cd ${APP_PATH} &&
                    pip install --upgrade pip &&
                    pip install -r requirements.txt
                "
                '''
            }
        }

        stage('Run API Tests') {
            steps {
                sh '''
                docker exec ${CONTAINER_NAME} bash -c "
                    cd ${APP_PATH} &&
                    mkdir -p reports &&
                    pytest --maxfail=1 --disable-warnings -q --html=reports/report.html
                "
                '''
            }
        }
    }

    post {
        always {
            sh '''
            echo "Copying reports back to Jenkins..."
            docker cp ${CONTAINER_NAME}:${APP_PATH}/reports ./reports || true
            '''
            archiveArtifacts artifacts: '**/reports/*.html', allowEmptyArchive: true
        }
    }
}
