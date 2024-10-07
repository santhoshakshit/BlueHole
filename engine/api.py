import requests

def get_joke():
    """Fetch a random joke from JokeAPI, excluding adult content."""
    url = "https://v2.jokeapi.dev/joke/Any"
    params = {
        'type': 'single',             # 'single' for a one-liner joke
        'blacklistFlags': 'nsfw,racist,sexist,explicit',  # Filter out adult and inappropriate content
        'lang': 'en'                  # Language (English)
    }
    response = requests.get(url, params=params)
    joke_data = response.json()
    
    if joke_data['type'] == 'single':
        return joke_data['joke']
    else:
        return "Could not retrieve a joke at this time."

def get_news(api_key, query='latest'):
    """Fetches news headlines based on the query using GNews API."""
    try:
        base_url = f"https://gnews.io/api/v4/search?q={query}&token={api_key}"
        response = requests.get(base_url)
        print(f"API Response Status Code: {response.status_code}")  # Debug statement
        print(f"API Response Text: {response.text}")  # Debug statement

        if response.status_code == 200:
            data = response.json()
            articles = data.get('articles', [])
            if articles:
                # Get top 3 articles and summarize them
                headlines = [f"{article['title']}: {article['description']}" for article in articles[:3]]
                news_summary = " ".join(headlines)
                
                # Limit the summary to 2-3 sentences
                sentences = news_summary.split('.')
                limited_summary = '.'.join(sentences[:3]) + '.'
                
                return f"Here are some headlines about {query}: {limited_summary}"
            else:
                return f"No news articles found about {query}."
        else:
            return f"Error: {data.get('message', 'Unable to fetch news data')}"
    except Exception as e:
        return f"An error occurred: {str(e)}"

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
