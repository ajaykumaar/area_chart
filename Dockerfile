from python:3.7-slim-stretch


WORKDIR /area_chart

ADD . /area_chart

#ADD requirements.txt /area_chart/

#ADD app.py /area_chart/


RUN pip install -r requirements.txt


