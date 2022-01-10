pipeline {
  agent any
  environment {
    registry = "gouravas/jenkins-assignment"
    registryCredential = 'dockerhub'
    dockerImage = ''
    EMAIL_TO = "gouravsaini@sigmoidanalytics.com"
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
          sh "docker run -d --rm gouravas/jenkins-assignment:v1" // running the image
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
              echo "Pods and Deployments are availbale already, listed here."
              sh "kubectl get pods"
              sh "kubectl get deployments"
            }
          }   
        }
      }
    }
    success {
      emailext body: 'Check console output at $BUILD_URL to view the results. \n\n ${CHANGES} \n\n -------------------------------------------------- \n${BUILD_LOG, maxLines=100, escapeHtml=false}', 
        to: "${EMAIL_TO}", 
        subject: 'Build Success in Jenkins: $PROJECT_NAME - #$BUILD_NUMBER'
    }
        
    failure {
      emailext body: 'Check console output at $BUILD_URL to view the results. \n\n ${CHANGES} \n\n -------------------------------------------------- \n${BUILD_LOG, maxLines=100, escapeHtml=false}', 
        to: "${EMAIL_TO}", 
        subject: 'Build failed in Jenkins: $PROJECT_NAME - #$BUILD_NUMBER'
    }
  }
}
