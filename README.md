# Practical SFIA project #

Micro-sevice oriented arhitecture application that generates passwords upon a set of predefined rules.  

#### Content ####  
* [Introduction](https://github.com/AlinaDenisaB/SFIAproject2/blob/master/README.md#introduction)  
 * [Overview](https://github.com/AlinaDenisaB/SFIAproject2/blob/master/README.md#overview)  
 * [User Stories](https://github.com/AlinaDenisaB/SFIAproject2/blob/master/README.md#user-stories)
 * [Risk Assessment](https://github.com/AlinaDenisaB/SFIAproject2/blob/master/README.md#risk-assessment)
 * [ERD](https://github.com/AlinaDenisaB/SFIAproject2/blob/master/README.md#erd)
 * [CI Pipeline](https://github.com/AlinaDenisaB/SFIAproject2/blob/master/README.md#ci-pipeline)
 
* [Architecture - Micro Services](https://github.com/AlinaDenisaB/SFIAproject2/blob/master/README.md#arhitecture-micro-services)  
  * [Service #1](https://github.com/AlinaDenisaB/SFIAproject2/blob/master/README.md#service-#1)
  * [Service #2](https://github.com/AlinaDenisaB/SFIAproject2/blob/master/README.md#service-#2)  
  * [Service #3](https://github.com/AlinaDenisaB/SFIAproject2/blob/master/README.md#service-#3)
  * [Service #4](https://github.com/AlinaDenisaB/SFIAproject2/blob/master/README.md#service-#4)  
  
* [User Journey](https://github.com/AlinaDenisaB/SFIAproject2/blob/master/README.md#user-journey)  
* [Ansible Playbook](https://github.com/AlinaDenisaB/SFIAproject2/blob/master/README.md#ansible-playbook) 
* [Test Log](https://github.com/AlinaDenisaB/SFIAproject2/blob/master/README.md#tests-log)
* [Demonstration](https://github.com/AlinaDenisaB/SFIAproject2/blob/master/README.md#demonstration)
* [Future Improvements](https://github.com/AlinaDenisaB/SFIAproject2/blob/master/README.md#future-improvements)

### Introduction ### 
The project aims to create a password generator using microservices that generate numbers, letters and special characters.
#### Overview ####
#### User stories ####
#### Risk Assessment ####
#### ERD ####
#### CI Pipeline ####

### Architecture - Micro Services ### 
  #### Service #1 ####
  The first service is responsible for the communicating with the with the other 4 services and for persisting data in an SQL database.
  #### Service #2 #### 
  The second service is a number generator, which randomly gives 3 numbers for the first implementation and 5 numbers for the second implementation.
  #### Service #3 ####
  The third service is a letter generator that gives 10 random letters for the first implementation and 15 random letters for the second implementation.
  #### Service #4 ####
  The fourth service generate 2 special chars for the first implementation and 3 for the second implementation.
  #### Service #5 ####
  The fifth service create passwords based upon the results of the service #2 + #3 + #4 and shuffle the letters, the numbers and the special chars.
### User Journey ### 
### Ansible Playbook ###

CI Pipeline

Used technologies:
* Git - Version Control System  
* Jenkins - CI Server  
* Azure Virtual Machines - cloud server
* Docker - Conteinerisation   
* Docker Swarm - Orchestration Tool
* Asana (Kanban board) - full expansion on tasks needed to complete the project  
  * This also provide a record of any issues or risks I face creating my project  
    [Asana Board](https://app.asana.com/0/1167646120844282/board)
### Tests Log ###
### Demonstration ###
link
### Future Improvements ### 
