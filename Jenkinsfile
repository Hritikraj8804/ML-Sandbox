pipeline {
    agent any 

    stages {
        stage('Checkout') {
            steps {
                git branch: 'ui1', url: 'https://github.com/Hritikraj8804/ML-Sandbox.git' 
            }
        }

        stage('Build') {
            steps {
                // Commands for building your model (e.g., Python commands)
                bat 'echo Building on Windows...'
                bat 'cd backend && python app.py'
            }
        }

    }
}