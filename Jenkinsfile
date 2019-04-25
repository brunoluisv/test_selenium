pipeline {
  agent any
  stages {
    stage{
      steps{
        withPythonEnv('Python3'){
          pip3 install selenium
          pip3 install pytest
          pip3 install nose
          pip3 install allure-pytest
          chmod 777 geckodriver.log
          py.test --alluredir=allure-results Test.py 
        }
      }
    }
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
  }
}
