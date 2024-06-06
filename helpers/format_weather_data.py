from datetime import timedelta, datetime, timezone


def format_weather_data(data):
    """
    Displays detailed weather information for a given set of weather data.

    Args:
        data (dict): The JSON response from the API containing the weather data.
    """
    if data.get('cod') != 200:
        return "Error:" + data.get('message', 'Unknown error occurred.')

    # Extracting relevant information from the JSON data
    city = data.get('name')
    country = data.get('sys', {}).get('country')
    lon = data.get('coord', {}).get('lon')
    lat = data.get('coord', {}).get('lat')

    weather = data.get('weather', [])[0].get('main')
    description = data.get('weather', [])[0].get('description')

    temperature = data.get('main', {}).get('temp')
    feels_like = data.get('main', {}).get('feels_like')
    temp_min = data.get('main', {}).get('temp_min')
    temp_max = data.get('main', {}).get('temp_max')

    pressure = data.get('main', {}).get('pressure')
    humidity = data.get('main', {}).get('humidity')
    wind_speed = data.get('wind', {}).get('speed')
    wind_deg = data.get('wind', {}).get('deg')
    visibility = data.get('visibility')
    cloudiness = data.get('clouds', {}).get('all')

    sunrise = data.get('sys', {}).get('sunrise')
    sunset = data.get('sys', {}).get('sunset')
    timezone_offset = data.get('timezone')

    # Create a timezone object with the correct offset
    local_tz = timezone(timedelta(seconds=timezone_offset))

    # Convert timestamps to local time with timezone-aware datetime objects
    sunrise_local = datetime.fromtimestamp(sunrise, local_tz).strftime('%Y-%m-%d %H:%M:%S')
    sunset_local = datetime.fromtimestamp(sunset, local_tz).strftime('%Y-%m-%d %H:%M:%S')

    # Displaying the weather information
    return f"""   
    Weather in {city}, {country} (Longitude: {lon}, Latitude: {lat}):
        Weather: {weather}
        Detail: {description}
        
        Temperature: {temperature}°C   (Feels like: {feels_like}°C)
        Min Temperature: {temp_min}°C
        Max Temperature: {temp_max}°C
        
        Pressure: {pressure} hPa
        Humidity: {humidity}%
    
        Visibility: {visibility} meters
        Cloudiness: {cloudiness}%
        
        Wind Speed: {wind_speed} m/s
        Wind Direction: {wind_deg}°
        
        Sunrise: {sunrise_local}
        Sunset: {sunset_local}
        """
