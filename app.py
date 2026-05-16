import os
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

API_KEY = os.getenv("API_KEY")
BASE_URL = "https://api.weatherapi.com/v1/current.json"

@app.route("/")
def home():
    return "Weather API is running! Use /weather?city=Delhi"
    
def get_weather(city):
    params = {"key": API_KEY, "q": city, "aqi": "no"}
    try:
        response = requests.get(BASE_URL, params=params, timeout=5)
        response.raise_for_status()
        data = response.json()
        return {
            "city": data["location"]["name"],
            "country": data["location"]["country"],
            "temp": data["current"]["temp_c"],
            "feels_like": data["current"]["feelslike_c"],
            "humidity": data["current"]["humidity"],
            "desc": data["current"]["condition"]["text"]
        }
    except Exception as e:
        print("Error:", e)
        return None

@app.route("/weather")
def weather():
    city = request.args.get("city")
    if not city:
        return jsonify({"error": "Please provide a city parameter"}), 400
    result = get_weather(city)
    return jsonify(result) if result else (jsonify({"error": "City not found"}), 404)
