# Sqlalchemy-challenge

Part 1: Analyse and Explore the Climate Data

**results has been saved in the climate_starter.jupyter notebook
1. In this section, you’ll use Python and SQLAlchemy to do a basic climate analysis and data exploration of your climate database. Specifically, you’ll use SQLAlchemy ORM queries, Pandas, and Matplotlib. To do so, complete the following steps:
2. Note that you’ll use the provided files (climate_starter.ipynb and hawaii.sqlite) to complete your climate analysis and data exploration.
3. Use the SQLAlchemy create_engine() function to connect to your SQLite database.
4. Use the SQLAlchemy automap_base() function to reflect your tables into classes, and then save references to the classes named station and measurement.
5. Link Python to the database by creating a SQLAlchemy session.
6. Close session at the end of your notebook.

Precipitation Analysis

1. Find the most recent date in the dataset.
2. Using that date, get the previous 12 months of precipitation data by querying the previous 12 months of data.
3. Select only the "date" and "prcp" values.
4. Load the query results into a Pandas DataFrame. Explicitly set the column names.
5. Sort the DataFrame values by "date".
6. Plot the results by using the DataFrame plot method
7. Use Pandas to print the summary statistics for the precipitation data.

Station Analysis
1. Design a query to calculate the total number of stations in the dataset.
2. Design a query to find the most-active stations (that is, the stations that have the most rows). To do so, complete the following steps:
   List the stations and observation counts in descending order.
   Answer the following question: which station id has the greatest number of observations?
   Using the most-active station id, calculate the lowest, highest, and average temperatures.
   Use functions such as func.min, func.max, func.avg, and func.count in your queries

3. Design a query to get the previous 12 months of temperature observation (TOBS) data. To do so, complete the following steps:
   Filter by the station that has the greatest number of observations.
   Query the previous 12 months of TOBS data for that station.
   Plot the results as a histogram with bins=12, as the following image shows:
   Close the session.

Part 2: Design the Climate App

** results have been saved in app.python change.
   Run the Flask application  in a command by using python app.py
To do so, use Flask to create your routes as follows:

/
Start at the homepage.

List all the available routes.

/api/v1.0/precipitation
Convert the query results to a dictionary by using date as the key and prcp as the value.

Return the JSON representation of your dictionary.

/api/v1.0/stations
Return a JSON list of stations from the dataset.
/api/v1.0/tobs
Query the dates and temperature observations of the most-active station for the previous year of data.

Return a JSON list of temperature observations for the previous year.

/api/v1.0/<start> and /api/v1.0/<start>/<end>
Return a JSON list of the minimum temperature, the average temperature, and the maximum temperature for a specified start or start-end range.

For a specified start, calculate TMIN, TAVG, and TMAX for all the dates greater than or equal to the start date.

For a specified start date and end date, calculate TMIN, TAVG, and TMAX for the dates from the start date to the end date, inclusive.

Hints
Join the station and measurement tables for some of the queries.

Use the Flask jsonify function to convert your API data to a valid JSON response object.


Testing the Flask Routes
Now that the application is running, we can test the different routes. Here’s a brief overview of what each route should return and how to access them:

Home Page

URL: http://127.0.0.1:5000/

Description: This should return a welcome message with a list of available routes.

Precipitation Data

URL: http://127.0.0.1:5000/api/v1.0/precipitation

Description: This route returns a JSON representation of precipitation data, with dates as keys and precipitation values as values.

Station Data

URL: http://127.0.0.1:5000/api/v1.0/stations

Description: This route returns a JSON list of all stations in the dataset.

Temperature Observations

URL: http://127.0.0.1:5000/api/v1.0/tobs

Description: This route returns a JSON list of temperature observations (TOBS) for the previous year for the most-active station.

Temperature Statistics for a Start Date

URL: http://127.0.0.1:5000/api/v1.0/<start>

Example: http://127.0.0.1:5000/api/v1.0/2017-01-01

Description: This route returns a JSON list of the minimum, average, and maximum temperature for all dates greater than or equal to the specified start date.

Temperature Statistics for a Date Range

URL: http://127.0.0.1:5000/api/v1.0/<start>/<end>

Example: http://127.0.0.1:5000/api/v1.0/2017-01-01/2017-12-31

Description: This route returns a JSON list of the minimum, average, and maximum temperature for dates between the specified start and end dates, inclusive.

Testing Steps
Open a Web Browser: Navigate to each of the URLs mentioned above to see the JSON responses.

Verify Data: Ensure that the returned JSON data matches the expectations based on the data in the database.

Everything is working correctly so I can see appropriate JSON responses for each route. 
