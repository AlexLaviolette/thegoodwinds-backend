# Local development server

run:
	docker image build -t goodwinds . && docker run -e OPEN_WEATHER_MAP_API_TOKEN -e "PORT=5000" --name goodwinds -p 5000:5000 -d goodwinds

stop:
	docker rm -f goodwinds | true

logs:
	docker logs -f goodwinds


# Heroku

heroku-deploy:
	heroku container:push web --app goodwinds && heroku container:release web --app goodwinds


heroku-logs:
	heroku logs --tail --app goodwinds