from flask import Flask, jsonify
from flask_cors import CORS
from services.weather_service import *
from datetime import datetime

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


# Return 7x24 grid, one per day, with 24 hours each
@app.route('/weather', methods=['GET'])
def get_weather_summary():
  weather_report = get_weather()
  print("TEST")
  # Default each hour to the day's default (we only get 2 days of actual hourly weather)
  summary = {}
  for day, weather in weather_report.daily.items():
    if (len(summary) >= 7): break
    summary[day] = [weather.to_json()] * 24

  # Fill in the hourly data we have
  for day, hours in weather_report.hourly.items():
    for weather in hours:
      hour = datetime.fromtimestamp(weather.dt).hour
      summary[day][hour] = weather.to_json()

  return {
    'current': weather_report.current.to_json(),
    'data': summary
  }


if __name__ == '__main__':
  app.run()
