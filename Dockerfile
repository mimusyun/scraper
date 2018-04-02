FROM python:3.6

WORKDIR /opt/scraper

ADD . .

RUN pip install -r requirements.txt

CMD [ "python", "./src/run.py" ]