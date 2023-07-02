# :metal:	Log Service
- Log service is a service whose aims is take logs from different microservice / or user logs and write a in a file system. 
- There will be one perodic job, running which reads that logs once the file_size greater than 10MB or every 30 seconds and write to sql, finally delete the current logs files after processing it. 


## High Level Design: 
![LogService](https://github-production-user-asset-6210df.s3.amazonaws.com/40069230/250387189-c254afa9-6026-47f0-8b8a-27a4c54da1b0.png)

## :computer: Tech Stack
    
* [Django](https://www.django-rest-framework.org/)
* [Postgres](https://www.postgresql.org//)
* [Python](https://www.python.org/)
* [Docker](https://www.docker.com/)



## :running_woman: Local Installation Guide : 

1. Clone the repository by using Git Client: 

         git clone https://github.com/palrohitg/logservice.git

2. To Setup and Run Application + DataBase + CRON: 

        chmod +m application_container_start.sh
        ./application_container_start.sh

3. To Setup and Run Load Testing / Request: 

        chmod +m test_container_start.sh
        ./test_container_start.sh


## Logs of Docker Shell 
![LogService](https://github-production-user-asset-6210df.s3.amazonaws.com/40069230/250387944-decd7b32-12a0-4ffe-ae77-329ebcfb549e.png)
![LogService](https://github-production-user-asset-6210df.s3.amazonaws.com/40069230/250387972-2aabc407-d806-41a4-a024-d3b8a56069e7.png)

## 📜 LICENSE

  [MIT](https://github.com/palrohitg/logservice.git) 