pipeline {
  agent any
  stages {
  	stage('Virtual Env'){
  		steps {
  			sh "mkdir project"
  			sh "cd project"
  			sh "python3 -m venv virtualenv"

  		}
  	}
    stage('Executando Test') {
      steps {
      	sh "cd virtualenv"
      	sh "pip3 install selenium && pip3 install pytest"
      	sh "cp ../test_iafox.py ."
        sh "pytest test_iafox.py"
      }
    }    
  }
}
