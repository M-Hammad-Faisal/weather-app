# Weather App

This repository contains two versions of a Weather App built with Python:

1. `Console-based Weather App`: A command-line interface (CLI) application.
2. `GUI-based Weather App`: A graphical user interface (GUI) application using Tkinter.

Both versions fetch and display weather information for a given location using the `OpenWeatherMap` API.

## Features

- Fetches current weather data for a specified location.
- Displays temperature, humidity, weather description, wind speed, cloudiness, sunrise, and sunset times.
- Simple and user-friendly interface for both CLI and GUI.

## Prerequisites

- `Python 3.12` installed on your machine.
- An `API key` from OpenWeatherMap. You can get it [here](https://home.openweathermap.org/users/sign_up).

## Installation

1. Clone the repository or download the code:
   ```bash
   git clone https://github.com/m-hammad-faisal/weather-app.git
   cd weather-app
   ```
2. Install the required Python packages:
    ```bash
   pip install -r requirements.txt
    ```
3. Make sure you have Tkinter installed. Tkinter is included with the standard Python distribution. If you encounter issues, you can install it via your package manager:
    - On Debian-based Linux distributions (like `Ubuntu`):
      ```bash
      sudo apt-get install python3-tk
      ```
    - On `macOS`:
      ```bash
      brew install python-tk
      ```
4. Replace `YOUR_API_KEY` in the code with your actual API key from OpenWeatherMap in both the console and GUI versions.

## CLI Weather App
### Usage
Open cloned repository in terminal and run the script:
   ```bash
   python -m weather_app_cli.weather_app
   ```

Follow the prompts to enter a location and receive the weather information.

### Code Overview
- `weather_app.py`: The main script for the console application.
#### Example
   ```text
   Enter a location (or 'exit' to quit): Lahore
   
    Weather in Lahore, PK (Longitude: 74.3436, Latitude: 31.5497):
        Weather: Haze
        Detail: haze
        
        Temperature: 35.99°C   (Feels like: 36.15°C)
        Min Temperature: 35.99°C
        Max Temperature: 36.72°C
        
        Pressure: 1004 hPa
        Humidity: 30%
    
        Visibility: 4000 meters
        Cloudiness: 40%
        
        Wind Speed: 4.12 m/s
        Wind Direction: 270°
        
        Sunrise: 2024-06-06 04:57:38
        Sunset: 2024-06-06 19:05:19
   ```

## GUI Weather App
### Usage
Open cloned repository in terminal and run the script:
   ```bash
   python -m weather_app_gui.weather_app
   ```
A window will appear prompting you to enter a location. Enter the name of the city or location and click "Get Weather". The weather information will be displayed in the window.

### Code Overview
- `weather_app.py`: The main script that creates and runs the Tkinter GUI.
- The GUI is designed and managed within a `WeatherApp` class to avoid the use of global variables and to keep the code organized.

### Main Functions
- `__init__(self, root)`: Initializes the GUI components.
- `get_weather(self)`: Fetches and displays the weather information for the entered location.

## Common Helper Functions
- `fetch_weather(api_key, location)`: Makes an API call to OpenWeatherMap and returns the weather data.
- `format_weather_data(data)`: Formats the fetched weather data for display.

## Contributing
Contributions are welcome! Please fork this repository and submit pull requests for any features or improvements.

## License
This project is licensed under the `MIT License`. See the LICENSE file for details.
