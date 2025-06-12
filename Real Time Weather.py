import tkinter as tk
from tkinter import messagebox
import requests

def get_weather():
    city = city_entry.get().strip()
    if not city:
        messagebox.showerror("Error", "Please enter a city name.")
        return

    api_key = "c6489bcf49b8568152b3304e4a97c805"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    try:
        response = requests.get(url)
        data = response.json()

        if response.status_code == 200:
            temp = data["main"]["temp"]
            desc = data["weather"][0]["description"].capitalize()
            humidity = data["main"]["humidity"]
            wind = data["wind"]["speed"]

            result = (f"Temperature: {temp}°C\n"
                      f"Weather: {desc}\n"
                      f"Humidity: {humidity}%\n"
                      f"Wind Speed: {wind} m/s")
            result_label.config(text=result)
        else:
            result_label.config(text="City not found or API error.")
    except Exception as e:
        result_label.config(text="Error fetching data.")
        print(e)


root = tk.Tk()
root.title("Weather App")
root.geometry("350x300")
root.config(bg="#e6f7ff")

tk.Label(root, text="Enter City Name:", font=("Times New Roman", 12), bg="#e6f7ff").pack(pady=10)

city_entry = tk.Entry(root, font=("Times New Roman", 14), justify='center')
city_entry.pack(pady=5)

tk.Button(root, text="Get Weather", command=get_weather, bg="#3399ff", fg="white",
          font=("Times New Roman", 12), width=15).pack(pady=10)

result_label = tk.Label(root, text="", font=("Times New Roman", 12), bg="#e6f7ff", justify="left")
result_label.pack(pady=20)

root.mainloop()
