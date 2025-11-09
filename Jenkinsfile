pipeline {
    agent any

    environment {
        CONTAINER_NAME = 'python-runner'
        APP_PATH = '/app'
    }

    stages {
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

        stage('Run Tests') {
            steps {
                sh '''
                docker exec ${CONTAINER_NAME} bash -c "
                    cd ${APP_PATH} &&
                    pytest -v
                "
                '''
            }
        }
    }
}
