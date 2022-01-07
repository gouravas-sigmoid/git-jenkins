pipeline {
  agent { dockerfile true }
  stages {
    stage('Docker Build') {
      agent any
      steps {
        sh 'docker build -t jenkins/assignment:v2 .'
      }
    }
  }
}
