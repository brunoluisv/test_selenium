pipeline {
  agent any
  stages {
    stage('Start Build'){
      steps{
        script{
          allure([
            includeProperties: false,
            jdk: '',
            properties: [],
            reportBuildPolicy: 'ALWAYS',
            results: [[path: 'allure-results']]
          ])
        }
      }
    }
    stage('Bla'){
      steps{
        withPythonEnv('Python3'){
          sh 'pip3 install selenium'
          sh 'pip3 install pytest'
          sh 'pip3 install nose'
          sh 'pip3 install allure-pytest'
          sh 'chmod 777 geckodriver.log'
          sh 'py.test --alluredir=allure-results Test.py' 
        }
      }
    }
  }
}
