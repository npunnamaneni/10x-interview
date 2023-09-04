from flask import Flask, request, jsonify
import csv

app = Flask(__name__)

# Read the CSV file into a list of dictionaries
weather_data = []
with open("seattle-weather.csv", mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        weather_data.append(row)

# GET endpoint for querying the weather data
@app.route("/query", methods=["GET"])
def query():
    limit = request.args.get("limit")
    date = request.args.get("date")
    weather = request.args.get("weather")

    # Filter data based on query parameters
    filtered_data = [d for d in weather_data if
                    (date is None or d['date'] == date) and
                    (weather is None or d['weather'] == weather)]

    # Apply limit if applicable
    if limit is not None:
        filtered_data = filtered_data[:int(limit)]

    return jsonify(filtered_data)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
