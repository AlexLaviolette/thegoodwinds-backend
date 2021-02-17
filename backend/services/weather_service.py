import requests
import os
import math
import time
from datetime import datetime
from collections import defaultdict

API_TOKEN = os.environ['OPEN_WEATHER_MAP_API_TOKEN']
BASE_ENDPOINT = "http://api.openweathermap.org/data/2.5/"

MS_TO_KMH = 3.6

# Contains current weather, as well as hourly weather reports for the next 2 days 
# and daily weather reports for the next 7 days
class WeatherSummary:
  def __init__(self):
    self.current = None
    self.hourly = defaultdict(lambda: [])
    self.daily = {}

  def to_json(self):
    return {
      'current': self.current.to_json(),
      'hourly': {k: [x.to_json() for x in v] for (k,v) in self.hourly.items()},
      'daily': {k: v.to_json() for (k,v) in self.daily.items()}
    }

# Basic weather report
class WeatherReport:
  def __init__(self, dt, temp, feels_like, wind_kmh, pop, icon):
    self.dt = dt
    self.temp = temp
    self.feels_like = feels_like
    self.wind_kmh = round(wind_kmh, 2)
    self.pop = pop
    self.weather_rating, self.wind_rating, self.pop_rating = get_weather_ratings(temp, wind_kmh, pop)
    self.icon = icon

  def to_json(self):
    return self.__dict__

def get_weather_report_current(lat, lon):
  endpoint = "%s/weather?lat=%s&lon=%s&appid=%s&units=metric" % (BASE_ENDPOINT, lat, lon, API_TOKEN)
  response = requests.get(endpoint)
  json = response.json()

  return WeatherReport(
    json['dt'],
    json['main']['temp'],
    json['main']['feels_like'],
    json['wind']['speed'] * MS_TO_KMH,
    0,
    json['weather'][0]['icon'])

# Returns the weather for today up until the current time
# This uses UTC, so we might get some weather for yesterday in our timezone
# The weather report endpoint only returns future weather, so we need this to complete today's weather
def get_weather_report_today_so_far(lat, lon):
  current_timestamp = int(time.time())
  endpoint = "%s/onecall/timemachine?lat=%s&lon=%s&appid=%s&dt=%s&units=metric" % (BASE_ENDPOINT, lat, lon, API_TOKEN, current_timestamp)
  response = requests.get(endpoint)
  json = response.json()

  return json

# Retrieves current, hourly and daily weather reports
# Returns hourly/daily grouped by day
def get_weather_report_hourly(lat, lon):
  endpoint = "%s/onecall?lat=%s&lon=%s&exclude=minutely&appid=%s&units=metric" % (BASE_ENDPOINT, lat, lon, API_TOKEN)
  response = requests.get(endpoint)
  json = response.json()

  weather_summary = WeatherSummary()

  weather_summary.current = WeatherReport(
    json['current']['dt'],
    json['current']['temp'],
    json['current']['feels_like'],
    json['current']['wind_speed'] * MS_TO_KMH,
    0,
    json['current']['weather'][0]['icon'])


  today = get_weather_report_today_so_far(lat, lon)
  for hourly in today['hourly']:
    dt = hourly['dt']
    date_info = datetime.fromtimestamp(dt)
    # We don't care about yesterday's weather data
    if (date_info.day >= datetime.now().day):
      date_key = str(date_info.date())
      temp = hourly['temp']
      feels_like = hourly['feels_like']
      wind_kmh = hourly['wind_speed'] * MS_TO_KMH
      pop = 0 # historical weather doesn't include pop
      icon = hourly['weather'][0]['icon']
      weather_report = WeatherReport(dt, temp, feels_like, wind_kmh, pop, icon)
      weather_summary.hourly[date_key].append(weather_report)

  for hourly in json['hourly']:
    dt = hourly['dt']
    date_info = datetime.fromtimestamp(dt)
    date_key = str(date_info.date())
    temp = hourly['temp']
    feels_like = hourly['feels_like']
    wind_kmh = hourly['wind_speed'] * MS_TO_KMH
    pop = hourly['pop']
    icon = hourly['weather'][0]['icon']
    weather_report = WeatherReport(dt, temp, feels_like, wind_kmh, pop, icon)
    weather_summary.hourly[date_key].append(weather_report)

  for daily in json['daily']:
    dt = daily['dt']
    date_info = datetime.fromtimestamp(dt)
    date_key = str(date_info.date())
    temp = daily['temp']['day']
    feels_like = daily['feels_like']['day']
    wind_kmh = daily['wind_speed'] * MS_TO_KMH
    pop = daily['pop']
    icon = daily['weather'][0]['icon']
    weather_report = WeatherReport(dt, temp, feels_like, wind_kmh, pop, icon)
    weather_summary.daily[date_key] = weather_report

  return weather_summary


# 0-10 = 1, 11-20 = 2, 21-30 = 3, 31-40 = 4, 41-50 = 5, 51+ = 6
def get_wind_rating(wind_kmh):
  return min(math.ceil(wind_kmh/10), 6)


# Below zero, assume snow which is more tolerable
def get_pop_rating(pop, temp):
  if (temp > 0):
    # Rain
    if (pop > 0.7): return 6
    elif (pop > 0.6): return 5
    elif (pop > 0.5): return 4
    elif (pop > 0.3): return 3
    elif (pop > 0.2): return 2
    else: return 1
  
  else:
    # Snow
    if (pop > 0.9): return 4
    elif (pop > 0.7): return 3
    elif (pop > 0.5): return 2
    else: return 1


# Returns (weather_rating, wind_rating, pop_rating). All integers from (1-6)
def get_weather_ratings(temp, wind_kmh, pop):
  wind_rating = get_wind_rating(wind_kmh)
  pop_rating = get_pop_rating(pop, temp)
  weather_rating = max(wind_rating, pop_rating)

  return (weather_rating, wind_rating, pop_rating)


