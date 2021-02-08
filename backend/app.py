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

def get_weather_by_hour():
  weather_report = get_weather()
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


# Return 7x24 grid, one per day, with 24 hours each
@app.route('/weather/hourly', methods=['GET'])
def get_weather_hourly():
  return get_weather_by_hour()

@app.route('/weather/chunked', methods=['GET'])
def get_weather_chunks():
  data = get_weather_by_hour()

  chunked = defaultdict(lambda: [])

  for day, hours in data['data'].items():
    previous_rating = 0
    for hour, weather in enumerate(hours): # hour is the index
      weather_rating = weather['weather_rating']
      if (weather_rating != previous_rating):
        chunk = {
          "weather_rating": weather_rating,
          "size": 1,
          "wind_rating": weather['wind_rating'],
          "pop_rating": weather["pop_rating"],
          "wind_kmh": weather["wind_kmh"],
          "pop": weather["pop"],
          "temp": weather["temp"]
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
      chunk['temp'] = str(round(chunk['temp'] / chunk['size'], 2))
      chunk['wind_kmh'] = str(round(chunk['wind_kmh'] / chunk['size'], 2))
      chunk['pop'] = str(round(chunk['pop'] / chunk['size'], 2))

  return chunked


if __name__ == '__main__':
  app.run()
