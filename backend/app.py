from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import os

app = Flask(__name__)
CORS(app)

API_KEY = os.environ.get('OPENWEATHER_API_KEY')
BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'

@app.route('/weather', methods=['GET'])
def get_weather():
    city = request.args.get('city')
    if not city:
        return jsonify({'error': 'City parameter is required'}), 400

    url = f'{BASE_URL}?q={city}&appid={API_KEY}&units=metric'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        #Bug: Intentionally dropping the wind speed
        #data.pop('wind', None)
        return jsonify(data)
    else:
        return jsonify({'error': 'City not found'}), response.status_code

if __name__ == '__main__':
    app.run(debug=True)
