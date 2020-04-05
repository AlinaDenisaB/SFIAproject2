pipeline {
    agent any
    stages{
      stage('Deploy'){
	steps{
	sh '''
		git clone https://github.com/AlinaDenisaB/SFIAproject2
		cd ./SFIAproject
		export version=V1
		docker stack deploy --compose-file docker-compose.yaml SFIAproject2
	'''
	}
     }
   }
}
