pipeline {
  agent any
  stages {
  	stage('Virtual Env'){
  		steps {
  			sh "virtualenv iafox_test"
  			sh "cd iafoxtest"
  			sh "pip install selenium"
  			sh "pip install pytest"
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
