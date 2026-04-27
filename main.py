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
def currentWeather(data, offset):
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

#get api key
apiKey = os.getenv("WEATHER_API_KEY")

#get weather from api
def getWeatherFromAPi(url):
    try:
        response = requests.get(url)
        data = response.json()

        if(data['cod'] == "404"):
            print(data['message'])
        
        else:
            offset = data['timezone']
            currentWeather(data, offset)

    except:
        print("Error Fetching Data!")



#get units for temperature
def getUnits():
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

    return units




#get units for temperature
units = getUnits()

cityName = input("Which city would you like to get the weather for today? ")
url = f"https://api.openweathermap.org/data/2.5/weather?q={cityName}&appid={apiKey}&units={units}"


choice = 0
while(choice !=4 ):
    #generating the menu
    print("What would you like to do today? ")
    print("1. Get Current Weather")
    print("2. Change Units")
    print("3. Search Another City")
    print("4. Exit")
    choice = int(input("Please enter your choice: "))
    print(choice)
    match choice:
        case 1:
            getWeatherFromAPi(url)

        case 2:
            units = getUnits()
            url = f"https://api.openweathermap.org/data/2.5/weather?q={cityName}&appid={apiKey}&units={units}"
            getWeatherFromAPi(url)

        case 3:
            cityName = input("Which city would you like to get the weather for today? ")
            url = f"https://api.openweathermap.org/data/2.5/weather?q={cityName}&appid={apiKey}&units={units}"
            getWeatherFromAPi(url)
        
        case 4:
            print("See You Again!")
        
        case _:
            print("Error in Choice")

    print("------------------------------------------------------------------------------------")
            



