import requests

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
