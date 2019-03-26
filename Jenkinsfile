pipeline {
  agent any
  stages {
    stage('Installing selenium') {
      steps {
        sh "pip install selenium"
      }
    }
    stage('Executando Test') {
      steps {
        sh "cp driver/geckodriver /usr/local/bin"
        sh "python test_iafox.py"
      }
    }    
  }
}
