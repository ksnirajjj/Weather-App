# Weather App

## Overview
This is a console based weather app built using Python. It allows you to enter the city and view the weather. 

## Features
- Search weather by city name
- View temperature and “feels like” temperature, humidity and wind speed
- Switch between Celsius and Fahrenheit
- Shows sunrise and sunset times
- Change city without restarting the app

## Requirements
Python 3
pip install requests

## Setup
1. Go to https://openweathermap.org/api and get your api key.
2. Set your API key as an environment variable:
   Mac/Linux:
   export WEATHER_API_KEY="your_api_key"
   
   Windows (Command Prompt):
   set WEATHER_API_KEY=your_api_key
   
   Windows (PowerShell):
   $env:WEATHER_API_KEY="your_api_key"



## How to run
python3 main.py
   
## Tech Stacks
- Python
- requests Library 
- OpenWeatherMap API
