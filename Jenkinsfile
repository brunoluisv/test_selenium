pipeline {
  agent any
  stages {
  	stage('Virtual Env'){
  		steps {
  			sh "virtualenv -p /usr/bin/python3.5 iafoxtest"
  			sh "pip3 install selenium"
  			sh "pip3 install pytest"
  		}
  	}
    stage('Executando Test') {
      steps {
        sh "pytest test_iafox.py"
      }
    }    
  }
}
