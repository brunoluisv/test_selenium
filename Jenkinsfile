pipeline {
  agent any
  stages {
    stage('Executando Test') {
      steps {
	sh "chmod 777 geckodriver.log"
        sh "python -m unittest discover --pattern=test_iafox.py"
      }
    }    
  }
}
