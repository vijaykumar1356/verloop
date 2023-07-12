# verloop
Weather API (JSON | XML reponses)

**Setup Instructions** 


* NOTE: You should have docker installed in your machine for running this application
* do git pull using the command `git clone git@github.com:vijaykumar1356/verloop.git`
* move to the project root directory `.../verloop` from file explorer or terminal
* create file `.env` at project root directory (i.e., verloop folder)
* add the api key in the format mentioned in `.env-sample`.
* We need an API KEY that we can get once you sign up with the website https://rapidapi.com/weatherapi/api/weatherapi-com
* run the command `docker-compose up -d --build`
* for checking the server logs `docker logs -f verloop-container`
* for navigating to docker container from host machine `docker exec -it verloop-container /bin/sh`
* to test the api from postman
  * url - `http://localhost/api/get-current-weather`
  * method - POST
  * request body - ex:- {"city": "Bangalore", "output_format": "json"}