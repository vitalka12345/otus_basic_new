# to run use:
# cd homework_05
# docker build --progress=plain . -t football-app
# docker -D run -p 5000:5000 football-app

FROM python:3.9-buster

EXPOSE 5000

WORKDIR /var/app/

RUN pip3 install virtualenv; python3 -m venv ./;

COPY requirements.txt ./

RUN pip3 install -r requirements.txt

COPY ./ ./

RUN FLASK_ENV=production; FLASK_APP=app.py;

CMD flask run --host=0.0.0.0 --port=5000
