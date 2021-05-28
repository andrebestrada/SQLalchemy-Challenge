import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify
from sqlalchemy.sql.expression import all_

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///hawaii.sqlite")
# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)
print(Base.classes.keys())

# Save reference to the table
measurement=Base.classes.measurement
station=Base.classes.station




#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all routes that are available."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation>"
    )


@app.route("/api/v1.0/precipitation")
def names():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of all temperatures"""
    # Query all passengers
    results = session.query(measurement.date,measurement.prcp).all()
    session.close()

    all_measurements=[]
    for date,temp in results:
        temp_dict={}
        temp_dict['date']=date
        temp_dict['temp']=temp
        all_measurements.append(temp_dict)
    
    return jsonify(all_measurements)


if __name__ == '__main__':
    app.run(debug=True)
