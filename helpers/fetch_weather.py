import requests


def fetch_weather(api_key, location):
    """
    Fetches weather data for a given location from the OpenWeatherMap API.

    Args:
        api_key (str): The API key for authenticating with the OpenWeatherMap API.
        location (str): The name of the location for which to fetch the weather data.

    Returns:
        dict: The JSON response from the API containing the weather data.
    """
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': location,
        'appid': api_key,
        'units': 'metric'
    }
    response = requests.get(base_url, params=params)
    if response.status_code != 200:
        return {'cod': response.status_code, 'message': response.reason}
    return response.json()
