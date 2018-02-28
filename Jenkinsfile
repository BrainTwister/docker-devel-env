#!groovy

pipeline {

  agent {
    label 'docker-devel'
  }

  options {
    timeout(time: 2, unit: 'HOURS')
  }

  stages {
    stage('Build') {
      steps {
        sh './build.py'
      }
    }
  }

  post {
    success {
      mail to: 'bernd.doser@braintwister.eu', subject: "SUCCESS: ${currentBuild.fullDisplayName}", body: "Success: ${env.BUILD_URL}"
    }
    failure {
      mail to: 'bernd.doser@braintwister.eu', subject: "FAILURE: ${currentBuild.fullDisplayName}", body: "Failure: ${env.BUILD_URL}"
    }
  }
}
