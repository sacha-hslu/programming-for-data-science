import sys
import requests

API_KEY: str = "AIzaSyCMUkN0FfmeSzIbhNg8PkMYd_ecYhBINnI"


def whereShouldWeEat():
    args = sys.argv[1:]
    query: str = "Restaurant"
    if len(args) > 0:
        query = args[0]
    print(request(query))


def request(query):
    response = requests.get("https://maps.googleapis.com/maps/api/place/queryautocomplete/json?input="
                            + query + "%20near%20par&key=" + API_KEY)
    print(response)
    print(response.json())


if __name__ == "__main__":
    whereShouldWeEat()
