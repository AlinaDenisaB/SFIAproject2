pipeline {
    agent any
    stages{
      stage('Deploy'){
	steps{
	sh '''
		rm -rf SFIAproject2
		git clone https://github.com/AlinaDenisaB/SFIAproject2
		cd ./SFIAproject2
		export version=V1
		docker stack deploy --compose-file docker-compose.yaml SFIAproject2
	'''
	}
     }
   }
}
