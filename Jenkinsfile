node {
    stage ('actualize') {
        steps{
            sshagent(credentials : ['c161ad1b-2fb7-4d4c-90a6-bf4592f7f76d']) {
                git branch: 'master', credentialsId: 'e8376588-61c0-4fc4-b3ab-43e119a47300', url: 'git@github.com:RafaelBM91/python-template.git'
            }
        }
    }
    stage ('build') {
        steps{
            sshagent(credentials : ['c161ad1b-2fb7-4d4c-90a6-bf4592f7f76d']) {
                sh 'make build'
            }
        }
    }
}
