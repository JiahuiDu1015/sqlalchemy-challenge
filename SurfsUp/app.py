# Import the dependencies.
from flask import Flask, jsonify
from sqlalchemy import create_engine, func
from sqlalchemy.orm import Session
from sqlalchemy.ext.automap import automap_base
import datetime as dt


#################################################
# Database Setup
#################################################

# Create engine using the `hawaii.sqlite` database file
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# Declare a Base using `automap_base()`
Base = automap_base()

# Use the Base class to reflect the database tables
Base.prepare(autoload_with=engine)

# Debug: Print out the table names
print("Available tables are:", Base.classes.keys())

# Assign the measurement class to a variable called `Measurement` and
# the station class to a variable called `Station`
try:
    Measurement = Base.classes.measurement
    Station = Base.classes.station
except AttributeError as e:
    print(f"Error: {e}")
    print("Available tables are: ", Base.classes.keys())

# Create a session
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)



#################################################
# Flask Routes
#################################################
@app.route("/")
def welcome():
    return (
        f"Welcome to the Climate App API!<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end><br/>"
    )

# Precipitation Route
def precipitation():
    # Query precipitation data
    results = session.query(Measurement.date, Measurement.prcp).all()
    
    # Convert to dictionary
    precipitation_data = {date: prcp for date, prcp in results}
    
    return jsonify(precipitation_data)

# Stations Route

@app.route("/api/v1.0/stations")
def stations():
    # Query all stations
    results = session.query(Station.station).all()
    
    # Convert to list
    stations = [result[0] for result in results]
    
    return jsonify(stations)

# TOBS Route
def tobs():
    # Calculate the date one year ago from the last data point in the database
    most_recent_date = session.query(Measurement.date).order_by(Measurement.date.desc()).first()[0]
    most_recent_date = dt.datetime.strptime(most_recent_date, '%Y-%m-%d')
    one_year_ago = most_recent_date - dt.timedelta(days=365)

    # Query the most active station's temperature observations for the last year
    most_active_station = session.query(Measurement.station,func.count(Measurement.station)).\
                          group_by(Measurement.station).\
                          order_by(func.count(Measurement.station).desc()).first()[0]
    results = session.query(Measurement.date, Measurement.tobs).\
              filter(Measurement.station == most_active_station).\
              filter(Measurement.date >= one_year_ago).all()

    # Convert to list of temperature observations
    tobs_data = [{date: tobs} for date, tobs in results]

    return jsonify(tobs_data)

# Start Date Route
@app.route("/api/v1.0/<start>")
def start(start):
    # Query the minimum, average, and maximum temperature for dates greater than or equal to the start date
    results = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).filter(Measurement.date >= start).all()
    
    temps = {
        "TMIN": results[0][0],
        "TAVG": results[0][1],
        "TMAX": results[0][2]
    }
    
    return jsonify(temps)

# Start-End Date Route
@app.route("/api/v1.0/<start>/<end>")
def start_end(start, end):
    # Query the minimum, average, and maximum temperature for dates between the start and end date inclusive
    results = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
              filter(Measurement.date >= start).\
              filter(Measurement.date <= end).all()
    
    temps = {
        "TMIN": results[0][0],
        "TAVG": results[0][1],
        "TMAX": results[0][2]
    }
    
    return jsonify(temps)

# Run the Application
if __name__ == "__main__":
    app.run(debug=True)