import sys

from helpers import fetch_weather,format_weather_data


def main():
    """
    Main function to run the Weather App.

    Prompts the user for a location and displays the weather information
    for the entered location. Allows the user to enter multiple locations
    or exit the app by typing 'exit'.
    """
    api_key = "YOUR_API_KEY"  # Replace with your actual API key

    if api_key == "YOUR_API_KEY":
        print("Please replace 'YOUR_API_KEY' in the code with your actual API key from OpenWeatherMap.")
        sys.exit(1)

    while True:
        # Prompt the user for a location
        location = input("Enter a location (or 'exit' to quit): ").strip()
        if location.lower() == 'exit':
            break

        # Fetch and display weather data for the entered location
        data = fetch_weather(api_key, location)
        formatted_data = format_weather_data(data)
        print(formatted_data)


if __name__ == "__main__":
    main()
