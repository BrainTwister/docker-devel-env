#!groovy

pipeline {

  agent {
    dockerfile {
      label 'docker-devel'
      args '-v /var/run/docker.sock:/var/run/docker.sock'
    }
  }

  options {
    timeout(time: 2, unit: 'HOURS')
  }

  stages {
    stage('Build') {
      steps {
        withCredentials([[$class: 'UsernamePasswordMultiBinding', credentialsId: 'dockerhub',
                          usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD']]) {
          sh './build.py -u $USERNAME -p $PASSWORD'
        }
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
