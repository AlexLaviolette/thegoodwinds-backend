from flask import Flask, request
from flask_cors import CORS
from services.weather_service import *
from datetime import datetime
from exceptions.custom_errors import *
from collections import defaultdict

import os

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# Heroku sets the port via env var
port = int(os.environ.get("PORT", 5000))

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


@app.errorhandler(OpenWeatherMapError)
def handle_open_weather_map_error(e):
  return "Could not fetch weather data.", 424


@app.route('/status', methods=['GET'])
def status():
  return {'status': 'ok'}


# Returns the current weather for specified location based on lat and lon
@app.route('/weather', methods=['GET'])
def get_current_weather():
  current = WeatherService(request.args.get('lat'), request.args.get('lon')).get_weather_report_current()
  current.temp = round(current.temp)
  current.wind_kmh = round(current.wind_kmh)
  return current.to_json()


def get_weather_by_hour(lat, lon):
  weather_report = WeatherService(lat, lon).get_weather_report_hourly()
  # Default each hour to the day's default (we only get 2 days of actual hourly weather)
  summary = {}
  for day, weather in weather_report.daily.items():
    if (len(summary) >= 4): break
    summary[day] = [weather.to_json()] * 24

  # Fill in the hourly data we have
  for day, hours in weather_report.hourly.items():
    for weather in hours:
      hour = datetime.utcfromtimestamp(weather.dt).hour
      summary[day][hour] = weather.to_json()

  return summary


# Return 7x24 grid, one per day, with 24 hours each
@app.route('/weather/hourly', methods=['GET'])
def get_weather_hourly():
  return get_weather_by_hour(request.args.get('lat'), request.args.get('lon'))


# Returns chunks grouped by weather rating.
@app.route('/weather/chunked', methods=['GET'])
def get_weather_chunks():
  hourly = get_weather_by_hour(request.args.get('lat'), request.args.get('lon'))

  daytime_start = int(request.args.get('start', -1))

  chunked = defaultdict(lambda: [])

  for day, hours in hourly.items():
    previous_rating = 0
    for hour, weather in enumerate(hours):  # hour is the index
      weather_rating = weather['weather_rating']
      # Different weather rating means the start of a new chunk
      # We also start a new chunk at daytime_start to allow for easy viewing
      if (weather_rating != previous_rating or hour == daytime_start):
        chunk = {
          "weather_rating": weather_rating,
          "size": 1,
          "start": hour,
          "wind_rating": weather['wind_rating'],
          "pop_rating": weather["pop_rating"],
          "wind_kmh": weather["wind_kmh"],
          "pop": weather["pop"],
          "temp": weather["temp"],
          "icon": weather["icon"],
          "is_morning": hour < daytime_start
        }
        chunked[day].append(chunk)
        previous_rating = weather_rating
      else:
        chunked[day][-1]['size'] = chunked[day][-1]['size'] + 1
        # Sum wind, pop, and temp so we can take average
        chunked[day][-1]['temp'] = chunked[day][-1]['temp'] + weather['temp']
        chunked[day][-1]['wind_kmh'] = chunked[day][-1]['wind_kmh'] + weather['wind_kmh']
        chunked[day][-1]['pop'] = chunked[day][-1]['pop'] + weather['pop']

  # Average out wind, temperatue, and pop
  for chunks in chunked.values():
    for chunk in chunks:
      chunk['temp'] = round(chunk['temp'] / chunk['size'])
      chunk['wind_kmh'] = round(chunk['wind_kmh'] / chunk['size'])
      chunk['pop'] = round(chunk['pop'] / chunk['size'] * 100)

  return chunked


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=port, debug=True)
