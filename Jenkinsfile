pipeline {
  agent any
  stages {
  	stage('Virtual Env'){
  		steps {
  			sh "virtualenv -p /usr/bin/python3.7 iafoxtest"
  			sh "cd iafoxtest"
  			sh "pip3 install --upgrade pip"
  			sh "pip3 install selenium"
  			sh "pip3 install pytest"
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
