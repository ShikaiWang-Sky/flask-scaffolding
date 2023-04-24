# Flask-Scaffolding

## Overview

This Scaffold is a simple Flask application that uses the following technologies:

- Flask
- Flask-SQLAlchemy
- sqlite3
- Firebase (As authentication provider)
- daisyUI (Tailwind CSS Framework)
- Jinja2 (Template Engine)
- pipenv (Virtual Environment)
- Python 3.11.0
- Black (Code Formatter)

## Installation

1. Clone this repository
2. Install pipenv
3. create a virtual environment
4. Install dependencies <br/>
   under the root directory of the project run the following command:

```bash
    pipenv install
```

5. Run the application

```bash
    # set the FLASK_APP environment variable
    export FLASK_APP="app:create_app('development')"
    # run the application
    flask run
```

## Usage

### Create new tables

1. Create a new model under the `app/models` directory
2. Use following command to create the table

```bash
    # open the flask shell
    flask shell
    # create the tables
    from app.extensions import db
    from app.models.post import Post
    db.create_all()
    # exit the shell
    exit()
```

### Create new routes

1. Create a new route under the `app/routes` directory
2. Create a blueprint as it is shown in the `app/routes/auth.py` file
3. Register the blueprint in the `app/__init__.py` file

### What should we do with .env file?

- The .env file is used to store the environment variables
- The .env file should not be pushed to the repository
- The .env file should be added to the .gitignore file
- Following command shows how to generate SECRET_KEY in .env file

```bash
    python -c 'import secrets; print(secrets.token_hex())'
```

### How to set up your Firebase Authentication Configurations?
You need to set up your Firebase Authentication Configurations under `config/firebase` folder <br/>
You should build two new json files: `firebaseAdminConfig.json` and `firebaseConfig.json` <br/>
- In the `firebaseAdminConfig.json` file you should add your Firebase Admin SDK configurations: <br/>
Export Admin SDK private key — Go to Project Overview -> Service Accounts -> Firebase Admin SDK, then select Python as the language and click generate new private key and your file will download. Do NOT share this file or upload it anywhere it allows total read and write access of your Firebase project. 
- In the `firebaseConfig.json` file you should add your Firebase SDK configurations: <br/>
Go to Project Overview -> Project Settings -> General -> Your apps -> Firebase SDK snippet -> Config and copy the config object and paste it in the `firebaseConfig.json` file. <br/>
Also you have to add your realtime database url to the `firebaseConfig.json` file since we use Pyrebase4 and the bug still not repaired.<br/>
You should add the url as `"databaseURL": "your realtime database url"`
