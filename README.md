# Short-url
A URL shortener redirects short URLs to long URLs
This project contain 2 projects: Django & Django rest framework 


![pici](https://github.com/aviv-b/short-url/blob/main/screenshots/success.PNG)

### Algorithm 
 - Encoding the url Id to base62 * (A-Z a-z 0-9)
        _Why not using Hash ? 
        _MD5 hash will generate 128 bit and only take the first 7 bits 
        _Therefor it doesnt generate unique id. 
 - Encoding length will be 7 digits long *
    * This will allow us generate 62^7 tokens ~ 3.5 billon  
 - To Create 7 digit long the id COUNTER will start from 10000000+1  

### Algorithm 

### Scaling Architecture 


### Tech Stack 
- Web pages: Python Django 
- Web API: Python Django rest freamwork 
- DB: Sqlite 
- Front: Html, Css, Bootsrap

