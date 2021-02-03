# Beer Api Manager
A small and simple project that offers an API to manage beers. 

## Table of contents
* [About](#about)
* [Inspiration](#inspiration)
* [Features](#features)
* [Technologies](#technologies)
* [Startup](#startup)
* [Tests](#tests)
* [Documentation](#documentation)
* [Usefull commands](#usefull-commands)
* [Status](#status)
* [Contact](#contact)

## About
The intention of doing this project was to understand how to develop the backend architecture using python, flask, sqllite.

## Inspiration
The knowledge acquired in this project was provided majority by the article ["Modern Test-Driven Development in Python"](https://testdriven.io/blog/modern-tdd/) written by Jan Giacomelli. 

Thanks a lot Jan Giacomelli!

## Features
List of features ready and TODOs for future development
* Create beer
* Update beer
* Delete beer
* Search beer by id

To-do list:
- [X] Make straightforward version works with tests
- [X] Make initial swagger documentation  
- [X] Detach routes from app
- [ ] Improve tests for unhappy path scenarios
- [ ] Create abstract factory for persistency layer
- [ ] Implement concrete persistency factory for Sqlalchemy
- [ ] dockerize application

## Technologies
* Python - https://www.python.org/
* Flask - https://flask.palletsprojects.com/en/1.1.x/
* PyTest - https://docs.pytest.org/en/stable/
* Swagger - https://swagger.io/
* Flask-Restplus - https://flask-restplus.readthedocs.io/en/stable/
* SQLite - https://www.sqlite.org/index.html

## Startup

#### Tools
You must install [python3](https://docs.python-guide.org/starting/install3/linux/). The link provides good documentation about this process on Linux.

#### Clone the repository
```sh
$ git clone https://github.com/tiagovbarreto/python_beer_api.git
```

#### Create the venv
```sh
$ cd python_beer_api
$ python3 -m venv venv/
```

### Activate venv
```sh
$ cd python_beer_api
$ source venv/bin/activate
```

#### Install dependencies
```sh
$ cd python_beer_api
$ pip install -r requirements.txt
```

#### Start database
```sh
$ cd python_beer_api
$ python init_db.py
```

#### Run application
```sh
cd python_beer_api
$ export FLASK_APP=src/app.py && export FLASK_ENV=development && flask run
```

## Tests
#### To run tests
```sh
$ python -m pytest test
```

## Documentation
#### To access swagger
```sh
http://localhost:5000
```

## Usefull commands
#### Activate venv
```sh
$ cd python_beer_api
source venv/bin/activate
```

#### Deactivate venv
```sh
$ deactivate
```

## Status
Project is: _started_

## Contact
Created by tiagovalentim@gmail.com - feel free to contact me!


