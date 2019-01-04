# BMAT ASSESSMENT

The project is deployed at http://bmat.miguelgimenez.tech/


PLEASE BE AWARE THAT I HAVE NEVER USED PYTHON OR ELASTIC SEARCH!!! 

I realize that the python code is ugly and might have mixed django rest framework methodologies, please be kind on your evaluation haha 
I havent had time to implement any tests , but have used docker, elastic search and deployed it on Amazon to make up for it (as I wanted to  learn new things while doing the project, I am a profficient tester and can implement the test if its needed)/

## PART 1:

**Stack: Docker, Django, ElasticSearch, Django Rest Framework, Postgresql**

To match the candidates from an in input report against the database I decided to find matches by using elastic search , to find matches the rule to follow is 
by fuzzy searching for title and artist (having a elastic search boost of 0.5 each, so both add up together to 1), exact search for isrc ( this will have default boost =1 ), and what i wanted to do is then if any of the previous have scored, take the length into account, right now it will take it into account havin a 0.05 boost. The match score will be the elastic search score ( i actually just stored the order aat which they came since they were sorted from more relevant) being the lowest number the highest score.

If the database had millons of sound recordings, then probably the seach would have to be done in a separate thread ( i still havent figured to do that on python), 
Sharding the database, maybe also giving different elastic search indexes depending on the record ( i havent digged in too deep into elastic search yet). 


## PART 2: 

**Stack: React (with redux for state management), Webpack, and for styling I chose material-ui.**

The features of the UI  are listing the matches for a list of records, being able to select the correct match, upload CSV files as existing records or inputs to the database, and matching previously matched records.

To improve the user experience there are many things that can be done, I tried to make it as user friendly as possible, and made it responsive ... But some features like offline availability ( by making it progressive and storing the queries the user made for posterior update when online), improving the ui and styles, adding an animation when the table collapses/uncollapses, code splitting for faster loading times ...




# Architecture:

The Project has the following structure:

## Pages:

Main views, they will usually render depending on the route, they usually will contain just organisms or widgets.


## Organisms (widgets):

This will be the components that are composed of different molecules(parts) they will usually be connected to redux,they will be class components as they will have their own functionality and methods
They dont need propTypes

## Molecules:

This components will be stateless, they will be the parts that make up the organisms and should have the props "drilled" to them,  PropTypes are very important on this components as they will "describe" the
way they should behave. 
They are not connected to redux.

## Atoms: 

Units, for example buttons that are used in more than one place


#INSTRUCTIONS


**RUNNING THE PROJECT (PRODUCTION MODE ,API IN AWS INSTANCE):**

The project can be run in production mode, with an aws ec2 instance with docker that contains the required containers to run the project( ELASTIC SEARCH , PYTHON AND POSTGRESQL).

to do so just run on the frontend:

    $ yarn 
    
    or
    
    $ npm install

to install dependencies and to run the project:

    $ npm start  

go to ``http://localhost:8080/``



**RUNNING IN DEVELOPMENT MODE**

You will have to populate the database through the UI by clicking on the upload buttons (for the app to work correctly you will have to upload both types of records)

**API**

To run the api you will have to have docker installed and run from the  :

    $ docker-compose up

**IMPORTANT!!!: with the container running and in the same folder run**:


    $ docker-compose run web python manage.py search_index --create


  from the folder with the Dockerfile (api)

**FRONTEND**

 Install dependencies and:  

    $ npm run dev
​    

go to ``http://localhost:8080/``


##TODO:


There are a lof of things there can be done to improve this projects:

**Improve Error Handling**
**Unit Testing**
**Integration (E2E) Testing**
**Offline access**


