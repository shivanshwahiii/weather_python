from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route("/weather")
def weather():
    city = request.args.get("city")
    result = get_weather(city)
    return jsonify(result if result else {"error": "City not found"})
