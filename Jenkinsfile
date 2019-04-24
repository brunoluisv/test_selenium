pipeline {
  agent any
  stages {
  	stage('Virtual Env'){
  		steps {
  			sh "virtualenv iafox_test"
  			sh "cd iafoxtest"
  			sh "pip3 install selenium"
  			sh "pip3 install pytest"
  		}
  	}
    stage('Executando Test') {
      steps {
      	sh "cd .."
      	sh "ls"
      	sh "cp test_iafox.py iafox_test"
      	sh "cd iafox_test"
        sh "pytest test_iafox.py"
      }
    }    
  }
}
