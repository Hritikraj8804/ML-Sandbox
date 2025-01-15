pipeline {
    agent any

    environment {
        VENV_DIR = 'venv'
    }

    stages {
        stage('Setup') {
            steps {
                script {
                    // Clean the workspace
                    deleteDir()
                }
                // Checkout the code from the repository
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                script {
                    // Create a virtual environment
                    sh 'python -m venv ${VENV_DIR}'
                    // Activate the virtual environment and install dependencies
                    sh '''
                        source ${VENV_DIR}/bin/activate
                        pip install --upgrade pip
                        pip install -r requirements.txt
                    '''
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    // Activate the virtual environment and run tests
                    sh '''
                        source ${VENV_DIR}/bin/activate
                        pytest --junitxml=test-results.xml
                    '''
                }
            }
            post {
                always {
                    // Archive test results
                    junit 'test-results.xml'
                }
            }
        }
    }

    post {
        always {
            // Clean up the workspace
            cleanWs()
        }
    }
}