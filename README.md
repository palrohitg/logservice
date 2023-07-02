# :metal:	Log Service
- Log service is a service whose aims is take logs from different microservice / or user logs and write a in a file system. 
- There will be one perodic job, running which reads that logs once the file_size greater than 10MB or every 30 seconds and write to sql, finally delete the current logs files after processing it. 


## :computer: Tech Stack
    
* [Django](https://www.django-rest-framework.org/)
* [Postgres](https://www.postgresql.org//)
* [Python](https://www.python.org/)
* [Docker](https://www.docker.com/)



## :running_woman: Local Installation Guide : 

1. Clone the repository by using Git Client: 

         git clone https://github.com/palrohitg/reviewscrapper.git

2. Make a virtual environment mandatory: 

         * install pip, pipenv
         * Python -m venv virtual_env_name
         * make the virtual env and activate it 

3. Install the Packages: 

        pip install -r requirements.txt

4. Configure the mongoDB not mandatory [mlab](https://mlab.com/) :
    
         create Cluster, User Access and Network if need to make changes to db.

5. Run the reviewscrapper and enjoy : 

        python app.py

6. Finally don't forget to put Star :sunglasses:

## :arrow_lower_right:	Outcome/Result:
  
  :ballot_box_with_check: Reduces the Customer time by 70% while spending time for checking review of the product.

  :ballot_box_with_check: Helps to Gather information how's customer feels about the specific product and provide better services from business point of view. 
  
  :ballot_box_with_check: It can be used for offline Saler(Mobile) who want to upscale their business online. And Figuring out which product their put on their portal which increase the sales.

## :dart:	Scope of Improvement : 

* :blossom: UI can more Interactive. 
* :blossom: Scrap the reivews from multiple sites.
* :blossom: More features can be added. 
* :blossom: Suggestion and feed-Back always welcome.


## :iphone:	Running Instance:


* :arrow_right: Live :beers:[vikas-review-scrapper](https://vikas-webscrappper-review.herokuapp.com/) :beers:
* **Note**: Site maybe down I m working :crossed_fingers:
* **Side Note**: As the flipkart site has different design for different kind of product the review-scrapper not able to fetch the record. we have implement the desing related to electronic items. 


## 📜 LICENSE

  [MIT](https://github.com/palrohitg/reviewscrapper/blob/master/LICENSE) 