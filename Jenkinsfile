pipeline {
  agent any
  stages {
      stage('Cloning Git') {
          steps {
              script {
                  withCredentials([gitUsernamePassword(credentialsId: 'github', gitToolName: 'Default'), usernamePassword(credentialsId: 'github', passwordVariable: 'GIT_PSWD', usernameVariable: 'GIT_USR_NAME')]) {
                      echo "Repository is cloned"
                      sh 'git fetch --all'
                  }    
              }
          }
      }
      stage('Building Image') {
        steps{
                script {
      
                    // remove the images those are previously built
                    sh "docker image prune --all"
                    //dockerImage = docker.build registry + ":$BUILD_NUMBER"
                    sh "docker build -t gouravas/jenkins-assignment:v1 ."
                    sh "docker run -d --rm -p 5000:5000 gouravas/jenkins-assignment:v1"
                    echo "A New Image has been built"
                }
            }
      stage('Push image') {
        steps {
            script {
                withCredentials([string(credentialsId: 'dockerhub_id', variable: 'dockerhub_pwd')]) {
                    sh "docker login -u gouravas -p ${dockerhub_pwd}"
                    echo "Logged in to Docker registry"
                    sh "docker push gouravas/jenkins-assignment:v1"       
                }
            }
        }
      }
   }
}
}
