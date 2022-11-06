from flask import Flask, config, render_template, request
from fredapi import Fred
import pandas as pd
import yaml
import datetime
import sys
import os 
import settings
import json
import plotly
import plotly.express as px

# Create FRED object
# https://github.com/mortada/fredapi
fred = Fred(settings.API_KEY)

today = datetime.date.today()
lastyear = today - datetime.timedelta(days=365)

def loadseries2():
    with open("config.yml", "r") as ymlfile:
        cfg = yaml.safe_load(ymlfile)
        series = cfg["series"]

    for series in cfg["series"]:
        print("Fetching series: %s" % series)
        i = fred.get_series_info(series)
        print(i)
        s = fred.get_series(series, observation_start=lastyear, observation_end=today)
        print(s.tail())


# if __name__ == "__main__":
#     loadseries2()
     
app = Flask(__name__) # create an app instance

 
@app.route('/callback', methods=['POST', 'GET'])
def cb():
    return gm(request.args.get('data'))
   
@app.route('/')
def index():
    return render_template(
      'index.html', 
      graphJSON=gm(),
      series_list=series_list(),
      series_info=series_info().title
    )
  
def series_list():
  with open("config.yml", "r") as ymlfile:
        cfg = yaml.safe_load(ymlfile)
        series_list = cfg["series"]
  
  return series_list
 
def series_info(series='SP500'):
  return fred.get_series_info(series)

def gm(series='SP500'):
    df = pd.DataFrame(
      fred.get_series(
        series, 
        observation_start=lastyear,
        observation_end=today
      )
    )

    fig = px.line(df)

    graphJSON = json.dumps(
    fig, cls=plotly.utils.PlotlyJSONEncoder)
    print(fig.data[0])
    #fig.data[0]['staticPlot']=True
    
    return graphJSON

if __name__ == "__main__": # on running python app.py directly as a script
  app.run('0.0.0.0',8080, debug=True)