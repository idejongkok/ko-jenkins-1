pipeline {
    agent any

    stages {
        // stage('Setup Python Env') {
        //     steps {
        //         sh '''
        //         python3 -m venv venv
        //         . venv/bin/activate
        //         pip install -r requirements.txt
        //         '''
        //     }
        // }

        stage('Run API Tests') {
            steps {
                sh '''
                python --version
                '''
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: '**/reports/*.html', allowEmptyArchive: true
        }
    }
}




