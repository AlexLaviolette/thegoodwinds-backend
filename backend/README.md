# Backend

The backend of this project uses [Python Flask](https://flask.palletsprojects.com/en/1.1.x/) to serve processed weather data.
It retrieves the weather data from https://openweathermap.org/

## Project setup

 1. Create a new virtual environment:
 `python3 -m venv /path/to/new/virtual/env`
 2. Source the virtual env:
 `source /path/to/new/virtual/env/bin/activate`
 3. Install dependencies:
 `pip install -r requirements.txt`
 4. Start the development server
`python app.py`

You should be able confirm things are working by checking the status  of the server at `http://localhost:5000/status`