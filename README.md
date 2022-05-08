# Short-url
A URL shortener redirects short URLs to long URLs
This project contain 2 projects: `Django` & `Django rest framework` 


![pici](https://github.com/aviv-b/short-url/blob/main/screenshots/success.PNG)

### Algorithm 
 - Encoding the url Id to `base62` including [a-z][A-Z][0-9] characters.
 
        Why not using Hash? 
        MD5 hash will generate 128 bit and we only take the first 7 bits 
        Therefor it doesn't generate unique id. 
 - Encoding length will be `7 digits long` 
 
       This will allow us generate 62^7 tokens ~ 3.5 billon tokens.
 - To create 7 digit long the id COUNTER will start from `10000000+1`  
 
### Base62 algorithm 
  
    Located in `helpers` as base62.py 
    Very eazy to understand, Including explanation and examples.
    
### Scaling Architecture
    We can use a distributed service Zookeeper to solve the various challenges of a distributed system 
    like a race condition, deadlock, or particle failure of data.
    Every database take 10 mil ranges.
    For example: 
      Db1 ranges [100000001, 200000000]  
      Db2 ranges [200000001, 300000000] 
      
    In case of failur we can replicate data of master to it’s slave
    If one of the database reaches its maximum range we can create new database 
    and Zookeeper will assign an unused counter range to this new database.

### Tech Stack 
- Web pages: Python Django 
- Web API: Python Django rest freamwork 
- DB: Sqlite 
- Front: html, css, bootstrap
- Docker-composer 

### Settings
- Located in `Settings.py` file.
- To change the initial server counter: `SERVER_ID_COUNTER  = 100000001`
- To change the defult url: `SERVER_BASE_URL = "http://localhost:8000"`



### Build
Use Docker-Compose to spin up containers `docker-compose up`

### Main Routes
 - Web route: `localhost:8000`
 - Api route: `localhost:8000/api`
      
 



