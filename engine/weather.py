import requests

def get_weather(city, api_key):
    """Fetches weather information for a specific city using Weatherstack API."""
    try:
        base_url = f"http://api.weatherstack.com/current?access_key={api_key}&query={city}"
        response = requests.get(base_url)
        print(f"API Response Status Code: {response.status_code}")  # Debug statement
        print(f"API Response Text: {response.text}")  # Debug statement

        if response.status_code == 200:
            data = response.json()
            current = data['current']
            temperature = current['temperature']
            weather_description = current['weather_descriptions'][0]  # List of descriptions
            humidity = current['humidity']
            wind_speed = current['wind_speed']

            weather_report = (f"The weather in {city} is currently {weather_description}, "
                              f"with a temperature of {temperature}°C, "
                              f"humidity at {humidity}%, "
                              f"and wind speed of {wind_speed} km/h.")
            return weather_report
        else:
            return f"Error: {data.get('error', {}).get('info', 'Unable to fetch weather data')}"
    except Exception as e:
        return f"An error occurred: {str(e)}"
