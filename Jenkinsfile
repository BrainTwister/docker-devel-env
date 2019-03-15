#!groovy

pipeline {

  agent {
    docker {
      image 'braintwister/ubuntu-18.04-docker-18.09'
      args '-v /var/run/docker.sock:/var/run/docker.sock -e DOCKER_CONFIG=/tmp'
      alwaysPull true
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
          script {
            if (env.BRANCH_NAME == 'master') {
                sh './build.py -vv -u $USERNAME -p $PASSWORD'
            } else {
                sh './build.py -vv'
            }
          }
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
