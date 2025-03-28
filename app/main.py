import os
import requests


URL = "http://api.weatherapi.com/v1/current.json"
FILTERING = "Paris"
KEY = os.environ.get("API_KEY")


def get_weather() -> dict:
    params = {"key": KEY, "q": FILTERING}
    response = requests.get(URL, params=params)
    return response.json()


if __name__ == "__main__":
    get_weather()
