# Deploy ML model with Flask + Docker

## Description
The real estate company "ImmoEliza" is really happy about your regression model. They would like you to create an API to let their web-developers create a website around it.

## Usage
👉  Send POST request to `/predict` endpoint according to the [documentation](https://immo-eliza-flask-api.herokuapp.com/predict), it will return the prediction price of the property.

- `/predict endpoint`: `https://immo-eliza-flask-api.herokuapp.com/predict`
- [JSON format documentation](https://immo-eliza-flask-api.herokuapp.com/predict)

## Tooling
- flask
- docker
- heroku
- scikit learn
- pandas

## Installation
```bash
$ python -m venv venv
$ . venv/bin/activate
$ pip install -r requirements.txt
```

## Project Layout
```
project/
    model/
        *.pkl
    predict/
        prediction.py
    preprocessing/
        cleaning_data.py
    vendors/
        utils.py
        schema.py
    .gitignore
    Dockerfile
    Procfile
    requirements
    app.py
```
- The `models` folder contains linear regression model that predict property's price.
- The `preprocessing` handles the user input and transforms them  to match model required fields accordingly.
- The `predict` handles the prediction of price.
- The `vendors` folders contains application's utilities.

## Timeline
Repository: challenge-api-deployment
Solo Project
Duration: 5 days
Deadline: 01/04/2022 16:00 (code + email sent)
