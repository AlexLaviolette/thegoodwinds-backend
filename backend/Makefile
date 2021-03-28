run:
	docker image build -t goodwinds . && docker run -e OPEN_WEATHER_MAP_API_TOKEN --name goodwinds -p 5000:5000 -d goodwinds

stop:
	docker rm -f goodwinds | true

logs:
	docker logs -f goodwinds