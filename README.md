# Backend

The backend of this project uses [Python Flask](https://flask.palletsprojects.com/en/1.1.x/) to serve processed weather data.

It retrieves the weather data from https://openweathermap.org/

## Project setup
The backend app is setup to run in a container using Docker. A [Makefile](https://github.com/AlexLaviolette/goodwinds/blob/main/backend/Makefile) has been setup to provide shortcuts to common commands.

 1. Install Docker
 https://docs.docker.com/get-docker/
 2. Build and run the development server
 `make run`

You should be able confirm things are working by checking the status  of the server at `http://localhost:5000/status`.



## Makefile commands
`make run`: Build the image and start the container

`make stop`: Stop and remove the container

`make logs`: Tail application logs

[Full Makefile found here.](https://github.com/AlexLaviolette/goodwinds/blob/main/backend/Makefile)