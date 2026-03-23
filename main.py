import os
import requests

apiKey = os.getenv("WEATHER_API_KEY")

cityName = input("Which city would you like to get the weather for today? ")

url = f"https://api.openweathermap.org/data/2.5/weather?q={cityName}&appid={apiKey}&units=metric"

response = requests.get(url)
data = response.json()

print("--------------------------------------------------------------")
print(f"Showing weather for {cityName}")
print(f"Temperature: {data['main']['temp']}")
print(f"Feels like: {data['main']['feels_like']}")
print(f"Weather Conditions: {data['weather'][0]['description']}")
print(f"Humidity: {data['main']['humidity']}")
print(f"Wind Speed: {data['wind']['speed']}")




