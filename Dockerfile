FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /logservice
COPY requirements.txt /logservice/
RUN pip install -r requirements.txt
COPY . /logservice/
