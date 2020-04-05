pipeline{
    agent any
	environment
	{
		version = "${env.version}"
	}
	stages{
		stage("Update git repository") {
		steps{sh '''
                sudo su - jenkins
                cd SFIAproject2
                git checkout develop-playbook
                git pull
                echo "${version}"
                '''
			}
		}
		stage("Build") {
		steps{sh '''
                sudo su - jenkins
                cd SFIAproject2
                export version="${version}"
                docker-compose build
                docker-compose push
                '''
			}
		}
		stage("Deploy") {
			steps{sh '''ssh ansible-app << EOF
                sudo su - jenkins
                cd SFIAproject2
                git pull
                export version="${version}"
                docker stack deploy --compose-file docker-compose.yaml stack
                '''
			}
		}
	}
}
