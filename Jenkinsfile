pipeline {
  agent any
  environment {
    registry = "gouravas/jenkins-assignment"
    registryCredential = 'dockerhub'
    dockerImage = ''
  }
  stages {
    stage('Cloning Git') {
      steps {
        script {
          withCredentials([gitUsernamePassword(credentialsId: 'github', gitToolName: 'Default'), usernamePassword(credentialsId: 'github', passwordVariable: 'GIT_PSWD', usernameVariable: 'GIT_USR_NAME')]) {
            sh 'git fetch --all'    // git credentials provided using variable
            echo "Repository is Fetched"
          }    
        }
      }
    }
    stage('Building Image') {
      steps{
        script {
          sh "docker image prune --all"  // remove the images those are previously built
          sh "docker build -t gouravas/jenkins-assignment:v1 ." // building an image
          sh "docker run -d --rm -p 5000:5000 gouravas/jenkins-assignment:v1" // running the image
          echo "A New Image has been built"
        }
      }
    }
    stage('Push image') {
      steps {
        script {
          withCredentials([string(credentialsId: 'dockerhub_id', variable: 'dockerhub_pwd')]) {
            sh "docker login -u gouravas -p ${dockerhub_pwd}"  //dockerhub credentials provided using variable
            echo "Logged in to Docker registry"
            sh "docker push gouravas/jenkins-assignment:v1"       
          }
        }
      }
    }
    stage('Deploying nginx') {
      steps {
        script {
          kubeconfig(credentialsId: 'k8s_id', serverUrl: 'https://192.168.49.2:8443') {
            try {
              sh "kubectl create -f deployment.yaml"
              echo "Successfully Deployed."
              sh "kubectl get pods"
              sh "kubectl get deployments"
            }
            catch (err) {
              echo "Already Listed"
              sh "kubectl get pods"
              sh "kubectl get deployments"
            }
          }   
        }
      }
    }
    stage('Listing') {
      steps {
        script {
          echo "DONE"
        }    
      }
    }
  }
}
