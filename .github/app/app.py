from flask import Flask
from fredapi import Fred
import pandas as pd
import yaml
import datetime
import sys
import os 
import settings


# Create FRED object
# https://github.com/mortada/fredapi
fred = Fred(settings.API_KEY)

today = datetime.date.today()
lastyear = today - datetime.timedelta(days=365)

def loadseries(*args):
    with open("config.yml", "r") as ymlfile:
        cfg = yaml.safe_load(ymlfile)
        series = cfg["series"]

    for series in cfg["series"]:
        print("Fetching series: %s" % series)
        i = fred.get_series_info(series)
        print(i)
        s = fred.get_series(series, observation_start=lastyear, observation_end=today)
        print(s.tail())

if __name__ == "__main__":
    loadseries()

# app = Flask(__name__) # create an app instance

# @app.route("/") # at the end point /
# def hello(): # call method hello
#     return "Hello world" # which returns hello world

# @app.route("/<name>") # at the end point /<name> where name is user input
# def hello_name(name): # call method hello_name
#     return "Hello "+ name # which returns "hello" plus the user input string

# if __name__ == "__main__": # on running python app.py directly as a script
#     app.run(debug=True) # run the flask app