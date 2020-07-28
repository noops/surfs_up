#dependencies
import datetime as dt
import pandas as pd 
import numpy as np
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func 
from flask import Flask, jsonify

#create engine
engine = create_engine("sqlite:///hawaii.sqlite")

#reflect DB into our classes
Base = automap_base()
#reflect tables
Base.prepare(engine, reflect=True)
#save table references
Measurement = Base.classes.measurement
Station = Base.classes.station 
#create link from DB to python
session = Session(engine)



#define app for flask application
app = Flask(__name__)
@app.route('/')
def welcome():
    return(
    '''
    Welcome to the Climate Analysis API
    Available Routes:
    /api/v1.0/precipitation
    /api/v1.0/stations
    /api/v1.0/tobs
    /api/v1.0/temp/start/end
    ''')