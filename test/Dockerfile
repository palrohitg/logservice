FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /logservice
COPY load_test.py /logservice/
COPY . /test/
RUN pip install requests