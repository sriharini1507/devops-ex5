pipeline {
    agent any

    environment {
        STREAMLIT_SUPPRESS_PROMPT = 'true'
    }

    stages {

        stage('Clone Repo') {
            steps {
                git branch: 'main', url: 'https://github.com/sriharini1507/devops-ex5.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat "C:\\Users\\Harini\\AppData\\Local\\Programs\\Python\\Python312\\python.exe -m venv venv"
                bat "call venv\\Scripts\\activate && pip install -r requirements.txt"
            }
        }

        stage('Run Streamlit App') {
            steps {
                bat "call venv\\Scripts\\activate && python -m streamlit run streamlit_app.py --server.headless true"
            }
        }
    }
}
