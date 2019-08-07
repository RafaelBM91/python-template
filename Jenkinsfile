node {
    stage ('actualize') {
        git branch: 'master', credentialsId: 'e8376588-61c0-4fc4-b3ab-43e119a47300', url: 'git@github.com:RafaelBM91/python-template.git'
    }
    stage ('build') {
        sh 'make build'
    }
}
