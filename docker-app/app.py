"""program to create a web service that converts a CSV file into an API that exposes JSON"""
from flask import Flask, request, jsonify
import csv
import os
import datetime

app = Flask(__name__)

csv_file_path = "seattle-weather.csv"


# Read the CSV file
def read_csv_file():
    if not os.path.isfile(csv_file_path):
        return None  # Return None if the file is missing
    weather_data = []
    with open(csv_file_path, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            weather_data.append(row)
    return weather_data


# Define a function for handling errors
def handle_error(message, status_code):
    response = jsonify({"error": message})
    response.status_code = status_code
    return response


def is_valid_date(date):
    try:
        datetime.datetime.strptime(date, "%Y-%m-%d")
        return date
    except ValueError:
        return False


def is_valid_weather(weather):
    try:
        weather_types = set()
        with open(csv_file_path, mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                weather_types.add(row['weather'])
        if weather.strip() in weather_types:
            return True
    except:
        return False


def queried_data(weather_data, date, weather, precipitation, temp_max, temp_min, wind):
    data = [d for d in weather_data if
            (date is None or d['date'] == date) and
            (weather is None or d['weather'] == weather) and
            (wind is None or d['wind'] == wind) and
            (precipitation is None or d['precipitation'] == precipitation) and
            (temp_max is None or d['temp_max'] == temp_max) and
            (temp_min is None or d['temp_min'] == temp_min)]
    return data


# GET endpoint for querying the weather data
@app.route("/query", methods=["GET"])
def query():
    limit = request.args.get("limit")
    date = request.args.get("date")
    weather = request.args.get("weather")
    precipitation = request.args.get("precipitation")
    temp_max = request.args.get("temp_max")
    temp_min = request.args.get("temp_min")
    wind = request.args.get("wind")

    # CSV file data
    weather_data = read_csv_file()

    # Check if the CSV file is missing
    if weather_data is None:
        return handle_error("CSV file not found", 404)

    try:
        if date and not is_valid_date(date):
            return handle_error("Invalid date format", 400)

        if weather and not is_valid_weather(weather):
            return handle_error("Weather parameter is not valid", 400)

        filtered_data = queried_data(weather_data, date, weather, precipitation, temp_max, temp_min, wind)

        # Apply limit if applicable
        if limit is not None and int(limit) > 1:
            filtered_data = filtered_data[:int(limit)]

        return jsonify(filtered_data) if filtered_data else handle_error("Invalid query", 400)

    except Exception as e:
        app.logger.error(f"An error occurred: {str(e)}")
        return handle_error("Internal Server Error", 500)


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
