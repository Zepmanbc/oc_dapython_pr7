# Papyrobot 🤖 👴

[![Build Status](https://www.travis-ci.org/Zepmanbc/oc_dapython_pr7.png?branch=master)](https://www.travis-ci.org/Zepmanbc/oc_dapython_pr7)
[![Coverage Status](https://coveralls.io/repos/github/Zepmanbc/oc_dapython_pr7/badge.svg?branch=master&service=github)](https://coveralls.io/github/Zepmanbc/oc_dapython_pr7?branch=master)

OpenClassrooms' project n°7 from [Python Application Developper path](https://openclassrooms.com/fr/paths/68-developpeur-dapplication-python)

A Grandpy Robot answers your questions about places.

online version on Heroku : https://bc-ocdapythonpr7.herokuapp.com/

## Getting Started

Clone the projet

    git clone https://github.com/Zepmanbc/oc_dapython_pr7.git

Go in the folder and set the virtualenv (it will install dependencies)

    cd oc_dapython_pr7
    pipenv install

Create a file name `.env` and fill it with your personnal Google map Keys (replace `123456`).

    touch .env

/oc_dapython_pr7/.env

    GMAPKEY_FRONT=123456
    GMAPKEY_BACK=123456

You can use the same key, it depends the restrictions.

Set `app.py` executable

    sudo chmod +x app.py

## Run the application

    pipenv run app.py

The Flask server will run on http://127.0.0.1:5000/

## Running the tests

    pipenv run pytest

(You can run without pipenv if pytest is installed on your computer)

The tests files are in [papyrobot/test/](https://github.com/Zepmanbc/oc_dapython_pr7/tree/master/papyrobot/tests)

## Built With

* [Python 3.6](https://www.python.org/)
* [Flask](http://flask.pocoo.org/): Web Framework
* [pymediawiki](https://github.com/barrust/mediawiki): wrapper and parser for the MediaWiki API
* [googlemaps](https://github.com/googlemaps/google-maps-services-python): Client for Google Maps API
