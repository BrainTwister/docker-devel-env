#!groovy

pipeline {

  agent {
    dockerfile {
      args '-v /var/run/docker.sock:/var/run/docker.sock -e DOCKER_CONFIG=/tmp'
    }
  }

  options {
    timeout(time: 24, unit: 'HOURS')
    retry(3)
    disableConcurrentBuilds()
  }

  stages {
    stage('Build') {
      steps {
        withCredentials([[$class: 'UsernamePasswordMultiBinding', credentialsId: 'dockerhub',
                          usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD']]) {
          sh './build.py -v -u $USERNAME -p $PASSWORD'
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
