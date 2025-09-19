pipeline {
  agent any
  
  stages {
    stage('Checkout') {
      steps { checkout scm }
    }
    stage('Install deps') {
      steps {
        sh 'python -m pip install --upgrade pip'
        sh 'pip install -r requirements.txt'
      }
    }
    stage('Tests') {
      steps {
        sh 'pytest -q --maxfail=1 --junitxml=pytest.xml'
      }
      post {
        always { junit 'pytest.xml' }
      }
    }
    stage('Archive') {
      steps {
        archiveArtifacts artifacts: 'app/**/*.py,requirements.txt,pytest.xml', fingerprint: true
      }
    }
  }
}
