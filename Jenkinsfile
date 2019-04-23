pipeline {
  agent any
  stages {
    stage('Executando Test') {
      steps {
        sh "python -m unittest discover --pattern=test_iafox.py.py"
      }
    }    
  }
}
