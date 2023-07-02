import requests
import time

url = 'http://web:8000/api/v1/log/'

headers = {
    'Content-Type': 'application/json',
    'Cookie': 'csrftoken=YbL0TO3SDOuCBL2P5hsBfFZELGEL0TGdoEskwOjt3ZJFmc1AIt6xqZsNUEswJMTH'
}

data = {
    'id': 1234,
    'unix_ts': 1684129671,
    'user_id': 123456,
    'event_name': 'login'
}

requests_per_second = 10
duration_seconds = 10
total_requests = requests_per_second * duration_seconds

for i in range(total_requests):
    response = requests.post(url, headers=headers, json=data)
    print(f'Request {i+1}/{total_requests} - Status: {response.status_code}')
    time.sleep(1/requests_per_second)
