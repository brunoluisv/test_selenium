pipeline {
  agent any
  stages {
  	stage('Virtual Env'){
  		steps {
  			sh "virtualenv -p /usr/bin/python3.7 iafoxtest"
  			sh "cd iafoxtest"
  			sh "pip install selenium"
  			sh "pip install pytest"
  		}
  	}
    stage('Executando Test') {
      steps {
      	sh "cd .."
      	sh "ls"
      	sh "cp test_iafox.py iafoxtest"
      	sh "cd iafoxtest"
        sh "pytest test_iafox.py"
      }
    }    
  }
}
