from flask import Flask, request, jsonify
import requests
import json
import os

app = Flask(__name__)

# OpenWeatherMap API credentials
OPENWEATHER_API_KEY = 'be718214f625a9ae4064ffff922b9040'  # replace with your actual OpenWeatherMap API key

# Optional: Twilio Credentials (if you're testing SMS with Twilio)
# account_sid = 'your_twilio_account_sid'
# auth_token = 'your_twilio_auth_token'
# client = Client(account_sid, auth_token)

# Function to fetch live weather data
def fetch_weather_data(city_name):
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={OPENWEATHER_API_KEY}&units=metric"
    response = requests.get(base_url)
    return response.json()

# Function to check for severe weather conditions
def check_severe_weather(weather_data):
    weather_conditions = weather_data['weather'][0]['description']
    if 'storm' in weather_conditions or 'heavy rain' in weather_conditions:
        return True
    return False

# Optional: Function to send SMS alerts
def send_sms_alert(phone_number, message):
    # For sending SMS using phone's native SMS service (optional logic here)
    # Twilio example if you need it for testing
    # message = client.messages.create(
    #     body=message,
    #     from_='+your_twilio_phone_number',
    #     to=phone_number
    # )
    return True  # Simulating SMS sent

# API to return live weather data for Android app
@app.route('/get_weather', methods=['GET'])
def get_weather():
    city = request.args.get('city', 'London')  # Default to 'London' if city is not provided
    weather_data = fetch_weather_data(city)
    if 'main' in weather_data:  # Successful response from API
        return jsonify(weather_data)
    else:
        return jsonify({"error": "City not found"}), 404

# API to handle SMS alerts for severe weather conditions
@app.route('/alert', methods=['POST'])
def alert():
    phone_number = request.json.get('phone_number')
    city = request.json.get('city', 'London')  # Default city

    # Fetch weather data for the given city
    weather_data = fetch_weather_data(city)
    
    if 'main' in weather_data:
        # Check if severe weather conditions exist
        if check_severe_weather(weather_data):
            # Prepare SMS alert message
            message = f"Severe weather alert for {city}: {weather_data['weather'][0]['description']}"
            # Send SMS alert to the given phone number
            send_sms_alert(phone_number, message)
            return jsonify({"message": "Severe weather detected, SMS sent."})
        else:
            return jsonify({"message": "No severe weather detected."})
    else:
        return jsonify({"error": "City not found"}), 404

# API to test SMS sending without weather alert (for debugging)
@app.route('/test_sms', methods=['POST'])
def test_sms():
    phone_number = request.json.get('phone_number')
    message = "Test SMS from Weather Forecast System"
    send_sms_alert(phone_number, message)
    return jsonify({"message": "Test SMS sent."})

if __name__ == '__main__':
    app.run(debug=True)
