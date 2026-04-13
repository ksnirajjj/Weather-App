import os
import requests
from datetime import datetime, timezone, timedelta


#get today's date
def getDate(date, offset):
    months = ["", "January", "February", "March", "April", "May", "June", 
              "July", "August", "September", "October", "November", "December"]
    tz = timezone(timedelta(seconds=offset))
    tx_time = datetime.fromtimestamp(date, tz)
    year = tx_time.year
    month = tx_time.month
    day = tx_time.day
    return(f"{months[month]} {day}, {year}")

#convert date time to redable format
def convertdate(time, offset):
    amOrPm = "AM"
    tz = timezone(timedelta(seconds=offset))
    tx_time = datetime.fromtimestamp(time,tz)
    hour = tx_time.hour
    minute = tx_time.minute
    if(hour > 12):
        hour -= 12
        amOrPm = "PM"

    return(f"{hour}:{minute} {amOrPm}")

    
#display current weather
def currentWeather():
    print("--------------------------------------------------------------")
    print(f"Showing weather for {cityName} on {getDate(data['dt'],offset)}")
    print(f"Temperature: {data['main']['temp']}")
    print(f"Feels like: {data['main']['feels_like']}")
    print(f"Weather Conditions: {data['weather'][0]['description']}")
    print(f"Humidity: {data['main']['humidity']}")
    print(f"Wind Speed: {data['wind']['speed']}")
    print(f"Minimum Temperature: {data['main']['temp_min']}")
    print(f"Maximum Temperature: {data['main']['temp_max']}")
    print(f"Sunrise: {convertdate(data['sys']['sunrise'], offset)}")
    print(f"Sunset: {convertdate(data['sys']['sunset'], offset)}")


apiKey = os.getenv("WEATHER_API_KEY")

cityName = input("Which city would you like to get the weather for today? ")

while(True):
    units = input("Would you like Celcius or Farenheit? ")
    if (units.lower() == "celcius"):
        units = "metric"
        break; 
    elif (units.lower() == "farenheit"):
        units = "imperial"
        break; 
    else:
        print("Invalid Unit Chosen!")

#validating city name


url = f"https://api.openweathermap.org/data/2.5/weather?q={cityName}&appid={apiKey}&units={units}"


#checking if the api works
try:
    response = requests.get(url)
    data = response.json()

    if(data['cod'] == "404"):
        print(data['message'])
    
    else:
        offset = data['timezone']
        currentWeather()

except:
   print("Error Fetching Data!")

#display 




