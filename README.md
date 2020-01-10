<h1 align="center">RESTful API for Udacity coffee shop application :coffee:</h1>
<p>
  <img src="https://img.shields.io/badge/version-1.0-blue.svg?cacheSeconds=2592000" />
  <a href="https://github.com/wanderindev/u-cafe/blob/master/README.md">
    <img alt="Documentation" src="https://img.shields.io/badge/documentation-yes-brightgreen.svg" target="_blank" />
  </a>
  <a href="https://github.com/wanderindev/u-cafe/graphs/commit-activity">
    <img alt="Maintenance" src="https://img.shields.io/badge/Maintained%3F-yes-brightgreen.svg" target="_blank" />
  </a>
  <a href="https://github.com/wanderindev/u-cafe/blob/master/LICENSE.md">
    <img alt="License: MIT" src="https://img.shields.io/badge/License-MIT-yellow.svg" target="_blank" />
  </a>
  <a href="https://twitter.com/JavierFeliuA">
    <img alt="Twitter: JavierFeliuA" src="https://img.shields.io/twitter/follow/JavierFeliuA.svg?style=social" target="_blank" />
  </a>
</p>

>Coffee Shop Full Stack is the third project for the 2019 Udacity Full-stack Developer Nanodegree.  The project is
>associated with the _Identity and Access Management_ course.  Visit 
>[this repository](https://github.com/udacity/FSND/tree/master/projects/03_coffee_shop_full_stack/starter_code) 
>for the starter code and project instructions.

## Project overview
The project contains a working frontend and the starter code for a backend.

The work performed on the frontend was limited to adding values to ```environment.ts``` that allow the frontend to connect
to the backend and to the authentication service.

In the backend, I implemented the following methods in ```auth.py```: ```get_token_auth_header```, ```check_permissions```, ```verify_decode_jwt```,
and ```requires_auth```.  In ```api.py```, I implemented 5 endpoints and implemented error handling.  In ```models.py```, I added some functionality
to the Drink model.

## How to use

### Clone the repository
Open a terminal window, clone the repository and cd into the project root:
```sh
git clone https://github.com/wanderindev/u-cafe.git
cd u-cafe
``` 

### The backend
Create a virtual environment, and activate it:
```sh
python3 -m venv venv
. venv/bin/activate
```
Install the project requirements:
```sh
pip install -r backend/requirements.txt
```
Run the RESTful API:
```sh
cd backend/src
export FLASK_APP=run;
flask run --reload
```
### Testing the API with Postman
The project includes a Postman collection (```u-cafe.postman_collection.json```) and a 
Postman environment (```u-cafe.postman_environment.json```) within the backend directory.  To test the API with Postman, follow these steps:
* Open Postman.
* Click on ```Import```.
* Select both json files and click on open.
* Click on ```Runner```.  The Collection Runner will open.
* Select the ```u-cafe``` collection and the ```u-cafe``` environment.
* Scroll all the way down and click the ```Run u-cafe``` button.
The collection will make 19 requests to the different endpoint with manager,
barista, and public access.  There is no need to manually enter the tokens for
manager and barista.  The first two requests in the collection authenticates both
users and sets the tokens to environment variables.

### The frontend
Leave the backend running and open a new terminal window.  Go into the frontend
directory:
```sh
cd u-cafe/frontend
``` 
The Ionic Command Line Interface is required to serve and build the frontend. 
If needed, follow the instructions for installing the CLI at 
[Ionic Framework Docs](https://ionicframework.com/docs/installation/cli)

Once the Ionic CLI is set up, install the frontend dependencies:
```sh
npm install
```

Start the frontend:
```sh
ionic serve
```

Access the frontend at http://127.0.0.1:8100.  The credential for the manager is ```manager@wanderin.dev``` password ```Udacity-Cafe```.
The credential for the barista is ```barista@wanderin.dev``` password ```Udacity-Cafe```.

## References
[_Auth0 Authentication API_](https://auth0.com/docs/api/info#authentication-api)

 ## Author

👤 **Javier Feliu**

* Twitter: [@JavierFeliuA](https://twitter.com/JavierFeliuA)
* Github: [@wanderindev](https://github.com/wanderindev)

[Starter code](https://github.com/udacity/FSND/blob/master/projects/03_coffee_shop_full_stack/starter_code) 
provided by [Udacity](https://www.udacity.com/).

## Show your support

Give a ⭐️ if this project helped you!

## 📝 License

Copyright © 2019 [Javier Feliu](https://github.com/wanderindev).<br />

This project is [MIT](https://github.com/wanderindev/u-cafe/blob/master/LICENSE.md) licensed.

***
_I based this README on a template generated with ❤️ by [readme-md-generator](https://github.com/kefranabg/readme-md-generator)_