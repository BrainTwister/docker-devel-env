#!groovy

pipeline {

  agent {
    docker {
      image 'braintwister/ubuntu-18.04-docker-18.09'
      args '-u root -v /var/run/docker.sock:/var/run/docker.sock -e DOCKER_CONFIG=/tmp -e USER_ID=1000'
      alwaysPull true
    }
  }

  options {
    timeout(time: 24, unit: 'HOURS')
    disableConcurrentBuilds()
  }

  stages {
    stage('Build') {
      steps {
        withCredentials([[$class: 'UsernamePasswordMultiBinding', credentialsId: 'dockerhub',
                          usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD']]) {
          sh './build.py --latest -vv -u $USERNAME -p $PASSWORD'
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
