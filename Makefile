freeze:
	pipenv lock --requirements > requirements.txt

shell:
	pipenv shell

run:
	python app.py

shell-run:
	pipenv shell python app.py

test:
	pipenv shell python -m unittest discover -s tests -p "test_*.py"

cleanup:
	rm -rf **/*.pyc
	rm -rf **/__pycache__
	rm -rf __pycache__

docker-run:
	docker-compose up --build -d

docker-logs:
	docker-compose logs --follow --tail=100

docker-stop:
	docker-compose down

heroku-login:
	heroku container:login

heroku-deploy:
	heroku container:push web
	heroku container:release web