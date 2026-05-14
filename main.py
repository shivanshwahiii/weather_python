import requests

API_KEY = "d592e38b27d04e039f370855261405"
BASE_URL = "https://api.weatherapi.com/v1/current.json"

def get_weather(city):
    params = {
        "key": API_KEY,
        "q": city,
        "aqi": "no"   # optional: exclude air quality data
    }
    response = requests.get(BASE_URL, params=params)
    data = response.json()
    if response.status_code == 200:
        return {
            "city": data["location"]["name"],
            "country": data["location"]["country"],
            "temp": data["current"]["temp_c"],
            "feels_like": data["current"]["feelslike_c"],
            "humidity": data["current"]["humidity"],
            "desc": data["current"]["condition"]["text"]
        }
    else:
        return None

def main():
    print("=== Weather App ===")
    city = input("Enter city name: ")
    result = get_weather(city)
    if result:
        print(f"City: {result['city']}, {result['country']}")
        print(f"Temp: {result['temp']}°C")
        print(f"Feels like: {result['feels_like']}°C")
        print(f"Humidity: {result['humidity']}%")
        print(f"Weather: {result['desc']}")
    else:
        print("City not found! Check spelling.")

main()
