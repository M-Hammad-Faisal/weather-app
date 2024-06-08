import sys
import tkinter as tk
from tkinter import messagebox, font

from helpers import fetch_weather, format_weather_data

class WeatherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Weather App")
        self.root.geometry("500x400")
        self.root.configure(bg="#263238")

        self.api_key = 'YOUR_API_KEY'  # Replace with your actual API key

        if self.api_key == "YOUR_API_KEY":
            messagebox.showerror("Error", "Please replace 'YOUR_API_KEY' with your actual API key.")
            sys.exit(1)

        # Set font
        custom_font = font.Font(family="Helvetica", size=10)

        # Create and place frames
        self.input_frame = tk.Frame(root, padx=20, pady=20, bg="#263238")
        self.input_frame.pack(fill=tk.X)

        self.result_frame = tk.Frame(root, padx=20, pady=20, bg="#37474F")
        self.result_frame.pack(fill=tk.BOTH, expand=True)

        # Input widgets
        tk.Label(self.input_frame, text="Enter location:", font=custom_font, bg="#263238", fg="#FFFFFF").pack(side=tk.LEFT, padx=5, pady=5)
        self.location_entry = tk.Entry(self.input_frame, width=35, font=custom_font, bg="#37474F", fg="#FFFFFF", relief=tk.FLAT)
        self.location_entry.pack(side=tk.LEFT, padx=5, pady=5)
        self.get_weather_button = tk.Button(self.input_frame, text="Get Weather", command=self.get_weather, font=custom_font, bg="#FF6F00", fg="#FFFFFF", relief=tk.FLAT, padx=2, pady=2)
        self.get_weather_button.pack(side=tk.LEFT, padx=5, pady=5)

        # Result widgets
        self.result_text = tk.StringVar()
        result_label = tk.Label(self.result_frame, textvariable=self.result_text, justify=tk.LEFT, anchor="nw", font=custom_font, bg="#37474F", fg="#FFFFFF")
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
