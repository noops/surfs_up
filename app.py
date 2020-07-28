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
#create precipitation route
@app.route('/api/v1.0/precipitation')
def precipitation():
    prev_year = dt.datetime(2017,8,23)-dt.timedelta(days=365)
    precipitation = session.query(Measurement.date, Measurement.prcp).\
        filter(Measurement.date >= prev_year).all()
    precip = {date: prcp for date, prcp in precipitation}
    #jsonify results for readability
    return jsonify(precip)

#create stations route
@app.route('/api/v1.0/stations')
def stations():
    results = session.query(Station.station).all()
    #unravel results into one-dimensional array and convert to list
    stations = list(np.ravel(results))
    #jsonify results for readability
    return jsonify(stations=stations)

#create tobs route (temperature observations)
@app.route('/api/v1.0/tobs')
def temp_monthly():
    prev_year = dt.datetime(2017,8,23)-dt.timedelta(days=365)
    results = session.query(Measurement.tobs).\
        filter(Measurement.station == 'USC00519281').\
        filter(Measurement.date >= prev_year).all()
    #unravel results into one-dimensional array and convert to list
    temps = list(np.ravel(results))
    return jsonify(temps=temps)

#create routes for temps with ending and starting dates
@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")
def stats(start=None, end=None):
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]
    if not end:
        results = session.query(*sel).filter(Measurement.date <= start).all()
        temps = list(np.ravel(results))
        jsonify(temps)
    results = session.query(*sel).filter(Measurement.date >= start).filter(Measurement.date <= end).all()
    temps = list(np.ravel(results))
    return jsonify(temps=temps)
