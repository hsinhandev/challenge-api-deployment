# Deploy Flask API + Docker

## Description
The real estate company "ImmoEliza" is really happy about your regression model. They would like you to create an API to let their web-developers create a website around it.

## Installation
```bash
$ pip install -r requirements.txt
```

## Usage
## Project Layout

I think that the folder structure is self-explanatory, but let’s look at it part by part API Module

The API module will host our application code, from models, routes, schemas and controllers if needed (though I usually don’t create those).
```
project/
    api/
        model/
            *.pkl
        predict/
            prediction.py
        preprocessing/
            cleaning_data.py
        schema/
            __init__.py
            welcome.py
    .gitignore
    Dockerfile
    Procfile
    requirements
    app.py
```
- The `models` are the data descriptor of our application, in many cases related to the database model, for example when using sqlalchemy, though they can be any class which represents the structure of our data.
- The `routes` are the paths to our application (e.g. /api/home or /api/users) and it’s where we will define the route logic, data retrieval, insertion, updates, etc.
- The `schemas` are the views (serializers) for our data structures. We should have at least one schema per model. The schemas will have it’s own definition as we will see later.

## Timeline
Repository: challenge-api-deployment
Solo Project
Duration: 5 days
Deadline: 01/04/2022 16:00 (code + email sent)
