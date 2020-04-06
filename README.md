# Practical SFIA project #

Micro-sevice oriented arhitecture application that generates passwords upon a set of predefined rules.  

#### Content ####  
* [Introduction](https://github.com/AlinaDenisaB/SFIAproject2/blob/master/README.md#introduction)  
 * [Overview](https://github.com/AlinaDenisaB/SFIAproject2/blob/master/README.md#overview)  
 * [User Stories](https://github.com/AlinaDenisaB/SFIAproject2/blob/master/README.md#user-stories)
 * [Risk Assessment](https://github.com/AlinaDenisaB/SFIAproject2/blob/master/README.md#risk-assessment)
 * [ERD](https://github.com/AlinaDenisaB/SFIAproject2/blob/master/README.md#erd)
 
* [Architecture - Micro Services](https://github.com/AlinaDenisaB/SFIAproject2/blob/master/README.md#arhitecture-micro-services)  
  * [Service #1](https://github.com/AlinaDenisaB/SFIAproject2/blob/master/README.md#service-#1)
  * [Service #2](https://github.com/AlinaDenisaB/SFIAproject2/blob/master/README.md#service-#2)  
  * [Service #3](https://github.com/AlinaDenisaB/SFIAproject2/blob/master/README.md#service-#3)
  * [Service #4](https://github.com/AlinaDenisaB/SFIAproject2/blob/master/README.md#service-#4)  
  * [Service #5](https://github.com/AlinaDenisaB/SFIAproject2/blob/master/README.md#service-#5)
  
* [CI Pipeline](https://github.com/AlinaDenisaB/SFIAproject2/blob/master/README.md#ci-pipeline) 
* [Test Log](https://github.com/AlinaDenisaB/SFIAproject2/blob/master/README.md#tests-log)
* [Demonstration](https://github.com/AlinaDenisaB/SFIAproject2/blob/master/README.md#demonstration)
* [Future Improvements](https://github.com/AlinaDenisaB/SFIAproject2/blob/master/README.md#future-improvements)

### Introduction ### 
#### Overview ####
The project aims to create a password generator using microservices that generate numbers, letters and special characters.

#### User stories ####
* As an user, I want to be able to generate a password, so that I can have a secure password that includes letters, numbers and special characters.
* As an administrator, I want secure passwords, so that will be easier to protect the data of the users.

#### Risk Assessment ####
![RA](https://github.com/AlinaDenisaB/SFIAproject2/blob/master/Documentation/RiskAssessment.PNG)

#### ERD ####
![ERD](https://github.com/AlinaDenisaB/SFIAproject2/blob/master/Documentation/ERD.png)

# Architecture - Micro Services #
![Architecture](https://github.com/AlinaDenisaB/SFIAproject2/blob/master/Documentation/ServicesArhitecture.png)
  #### Service #1 ####
  The first service is responsible for the communicating with the other 4 services and for persisting data in an SQL database.
  #### Service #2 #### 
  The second service is a number generator, which randomly gives 3 numbers for the first implementation and 5 numbers for the second implementation.
  #### Service #3 ####
  The third service is a letter generator that gives 10 random letters for the first implementation and 15 random letters for the second implementation.
  #### Service #4 ####
  The fourth service generate 2 special chars for the first implementation and 3 for the second implementation.
  #### Service #5 ####
  The fifth service create passwords based upon the results of the service #2 + #3 + #4 and shuffle the letters, the numbers and the special chars. Hence, the result will be a password that is redirected to the frontend service and it changes every time the user press the button.

# CI Pipeline #
![CI_Pipeline](https://github.com/AlinaDenisaB/SFIAproject2/blob/master/Documentation/CI_Pipeline.png)

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
![TestsMicroservices](https://github.com/AlinaDenisaB/SFIAproject2/blob/master/Documentation/microservicesTests.PNG)  
![TestPassGen](https://github.com/AlinaDenisaB/SFIAproject2/blob/master/Documentation/backendTest.PNG)  
![TestFrontEnd](https://github.com/AlinaDenisaB/SFIAproject2/blob/master/Documentation/frontendTest.PNG) 

### Demonstration ###
[link_demo](51.104.244.89:5000)

### Future Improvements ### 
* As future improvements, I would add a few filters to the application so that the user has the posibility to build the password according to the preferences. So, the filters would be like: selecting the size of the password, with a plenty of options available or to generate a phrase that will help the user to remember the password.
