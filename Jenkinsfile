pipeline {
  agent { Dockerfile true }
  stages {
    stage('Docker Build') {
      agent any
      steps {
        sh 'docker build -t jenkins/assignment:v2 .'
      }
    }
  }
}
