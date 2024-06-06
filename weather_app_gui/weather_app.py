import sys
import tkinter as tk
from tkinter import messagebox, font

from helpers import fetch_weather, format_weather_data


class WeatherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Weather App")
        self.root.geometry("500x400")

        self.api_key = 'YOUR_API_KEY'  # Replace with your actual API key

        if self.api_key == "YOUR_API_KEY":
            print("Please replace 'YOUR_API_KEY' in the code with your actual API key from OpenWeatherMap.")
            sys.exit(1)

        # Set default font
        default_font = font.nametofont("TkDefaultFont")
        default_font.configure(size=11)

        # Create and place frames
        input_frame = tk.Frame(root, padx=10, pady=10)
        input_frame.pack(fill=tk.X)

        result_frame = tk.Frame(root, padx=10, pady=10)
        result_frame.pack(fill=tk.BOTH, expand=True)

        # Input widgets
        tk.Label(input_frame, text="Enter location:", font=("Arial", 12, "bold")).pack(side=tk.LEFT, padx=5, pady=5)

        self.location_entry = tk.Entry(input_frame, width=30, font=("Arial", 12))
        self.location_entry.pack(side=tk.LEFT, padx=5, pady=5)

        tk.Button(input_frame, text="Get Weather", command=self.get_weather, font=("Arial", 12)).pack(side=tk.LEFT,
                                                                                                      padx=5, pady=5)

        # Result widgets
        self.result_text = tk.StringVar()
        result_label = tk.Label(result_frame, textvariable=self.result_text, justify=tk.LEFT, anchor="nw",
                                font=("Arial", 12))
        result_label.pack(fill=tk.BOTH, expand=True)

    def get_weather(self):
        """
        Fetches and displays the weather information for the entered location.
        """
        location = self.location_entry.get()
        if not location:
            messagebox.showerror("Error", "Please enter a location.")
            return

        data = fetch_weather(self.api_key, location)
        weather_info = format_weather_data(data)

        if data.get('cod') != 200:
            messagebox.showerror("Error", weather_info)
        else:
            self.result_text.set(weather_info)


def main():
    root = tk.Tk()
    app = WeatherApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
