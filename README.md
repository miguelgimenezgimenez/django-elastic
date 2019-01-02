# BMAT ASSESSMENT

The project is deployed at http://bmat.miguelgimenez.tech/

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

**API**

To run the api you will have to have docker installed and  run:

    $ docker-compose up

  from the folder with the Dockerfile (api)

**FRONTEND**

 Install dependencies and:  

    $ npm run dev
    
 
go to ``http://localhost:8080/``






# Architecture:


Although this is a small project I have used an atomic architecture, consisting of pages, molecules,organisms, a layout and have added targets(dropzones) and sources(draggable elements),
since it has dragAndDrop functionality.


## Pages:


Main views, usually rendered depending on the route, render all types of components.


## Organisms:
  
Components that usually have children, molecules and basic components

  
## Molecules:

   
Components that render basic components.

## Targets:


Components that can be used as dropzones


## Sources:

   
Components that are draggable.

