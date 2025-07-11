🌤️ Weather App GUI using Python & Tkinter
This is a simple Python GUI application that displays the current weather of any city entered by the user. It fetches real-time weather data using the OpenWeatherMap API and displays it in a clean interface built with Tkinter.

📌 Features
GUI built with Tkinter

Live weather data using OpenWeatherMap API

Displays:

🌡️ Temperature

☁️ Weather description

💧 Humidity

🌬️ Wind speed

Error handling for invalid city names or network issues

Lightweight and easy to run

🚀 How to Run
Clone the repository or copy the .py file.

Install requirements (if not already):

bash
Copy
Edit
pip install requests
Get your API key from https://openweathermap.org/api

Update this line in your code with your key:

python
Copy
Edit
api_key = "your_api_key_here"
Run the app:

bash
Copy
Edit
python weather_gui.py
🧠 Technologies Used
Python 3.x

Tkinter (built-in)

OpenWeatherMap API

Requests library

🔒 API Note
This app uses a free-tier API key from OpenWeatherMap. Rate limits apply (60 calls per minute). Avoid spamming requests.

📂 Folder Structure
cpp
Copy
Edit
weather_gui/
├── weather_gui.py
├── README.md
└── requirements.txt  (optional)
🙌 Acknowledgement
Developed during my Summer Internship at BIT Mesra, Patna
Mentor: Dr. Ratnesh Mishra

📜 License
This project is open for learning and educational use.
