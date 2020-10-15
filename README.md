# heroku-flask-api

## Requirements

- python3.8
- pipenv
- docker
- docker-compose

## Development

1. Create `.env` file and setup the values. Check .env.example
2. Build docker image for docker compose `docker-compose --build`
3. Start the server `docker-compose up --build`

### Dependencies

After add a new dependency, run `pipenv lock --requirements > requirements.txt` before commit.

## Deployment

The project is deployed to heroku.

### Configure heroku

You have to configure heroku to use a container: `heroku stack:set container`

### Deploy to heroku

0. `heroku container:login`
1. `heroku container:push web --app XX`
2. `heroku container:release web --app XX` 

## References

- https://devcenter.heroku.com/articles/build-docker-images-heroku-yml
- https://github.com/flask-restful/flask-restful
