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
                bat "\"C:\\Users\\Harini\\AppData\\Local\\Programs\\Python\\Python310\\python.exe\" -m venv venv"
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







pipeline {
    agent any

    stages {
        stage('Clone Repo') {
            steps {
                git branch: 'main', url: 'https://github.com/PreethiPalani23/dev-lab-5.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat "\"C:\\Users\\Harini\\AppData\\Local\\Programs\\Python\\Python310\\python.exe\" -m venv venv"
                bat "call venv\\Scripts\\activate && python -m pip install --upgrade pip"
                bat "call venv\\Scripts\\activate && pip install streamlit"
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
