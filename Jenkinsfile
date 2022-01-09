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
}
