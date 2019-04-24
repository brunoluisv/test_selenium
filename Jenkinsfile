pipeline {
  agent any
  stages {
    stage('Executando Test') {
      steps {
	sh "chmod 777 geckodriver.log"
        sh "python test_iafox.py"
      }
    }    
  }
}
