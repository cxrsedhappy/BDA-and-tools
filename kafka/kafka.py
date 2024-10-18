import requests
from quixstreams import Application

response = requests.get(
    "https://api.open-meteo.com/v1/forecast",
        params={
            'latitude': 55.6,
            'longitude': 37.3,
            'current': 'temperature_2m'
        }
)
print(response.json())

app = Application(
    broker_address="localhost:9092",
    loglevel="DEBUG",
)

with app.get_producer() as producer:
    producer.produce(
        ...
    )