# BMAT ASSESSMENT


**RUNNING THE PROJECT:**

The project can be run in production mode, with an aws ec2 instance that contains the required containers to run the project( ELASTIC SEARCH , PYTHON AND POSTGRESQL).

to do so just run on the frontend:

    $ yarn 
    
    or
    
    $ npm install

to install dependencies and to run the project:

    $ npm start
    

**API**

 **AP**
 
  

    $ yarn 
    
    or
    
    $ npm install



    $ npm run dev
    
 
go to ``http://localhost:8080/``


** INSTALL PACKAGE **

 *In a react app :* 
 
  $ npm install https://miguelgimenezgimenez@bitbucket.org/miguelgimenezgimenez/draganddrop.git  
  
    or
    
  $ yarn add https://miguelgimenezgimenez@bitbucket.org/miguelgimenezgimenez/draganddrop.git  


  require package
  
  

     import DragAndDrop from 'bigfinite-dnd'



# Description

  According to the specifications I have created a package that renders a component which has 2 toolbars, on to select a widget and one to select a screen, the middle of the screen has a dropzone to place the widgets .

  I have used react-dnd to add the drag and drop functionality and material ui to style the components.

  The way i have decided to store the state in the app was to have an array indicating where each widget was, instead of each widget knowing its position , this way the app will be more performant since the time complexity will be  O(n)
  to render the grid with the widgets placed.
  

  There are 2 different webpack configurations:
  

## Webpack.config.js

  This webpack is used to run the project on the development mode to run the demo, the entry point will be src/demo.js (which has the reactdom and render methods)and it will bundle all dependencies, and create the html file.


## Webpack.prod.config.js

  This webpack is used to run bundle the standalone package , it will not bundle react or react-dom, the entry point will be src/index.js, and it wil bundle with a libraryTarget(universal module definition) so the module can be used as a standalone package


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


# Testing and PropTypes:


I have only had time to do a very simple test , and only given strict propTypes to the MenuList Component, but if I am given more time I can add proper tests and strict propTypes
