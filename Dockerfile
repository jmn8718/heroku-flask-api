FROM heroku/heroku:18

RUN apt-get update
RUN apt-get install python3 python3-pip -y

ENV APP_HOME /app
WORKDIR $APP_HOME

COPY ./requirements.txt /app

RUN pip3 install -r requirements.txt

COPY . /app

CMD ["python3", "app.py"]