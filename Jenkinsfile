pipeline {
  environment {
    registry = "gourvas/jenkins-assignment"
    registryCredential = 'dockerhub'
    dockerImage = ''
  }
  agent any
  stages {
    stage('Cloning Git') {
        steps {
            script {
                withCredentials([gitUsernamePassword(credentialsId: 'github', gitToolName: 'git-tool')]) {
                    echo "Repository is cloned"
                    sh 'git fetch --all'
                }    
            }
        }
    }
    stage('Building Image') {
        steps{
            script {
                echo "Image has been built"
                dockerImage = docker.build registry + ":$BUILD_NUMBER"
              sh "docker run --rm -p 5000:5000 $dockerImage"
            }
        }
    }
    stage('Push image') {
        steps {
            script {
                withCredentials([string(credentialsId: 'dockerhub_id', variable: 'dockerhub_pwd')]) {
                    sh "docker login -u gouravas -p ${dockerhub_pwd}"
                    echo "Logged in to Docker registry"
                    sh "docker build -t gouravas/jenkins-assignment:v1 ."
                    sh "docker push gouravas/jenkins-assignment:v1"       
                }
            }
        }
    }
    stage('Docker Logout') {
      steps{
        sh "docker logout"
      }
    }
    stage("Removing unwanted Images") {
        steps {
            script {
                sh "docker rmi $registry:$BUILD_NUMBER"
            }
        }
    }
  }
}
