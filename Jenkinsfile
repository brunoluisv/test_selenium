pipeline {
  agent any
  stages {
  	stage('Virtual Env'){
  		steps {
  			sh "virtualenv iafoxtest"
  			sh "source iafoxtest/bin/activate"
  			sh "pip install selenium"
  			sh "pip install pytest"
  		}
  	}
    stage('Executando Test') {
      steps {
        sh "pytest test_iafox.py"
      }
    }    
  }
}
