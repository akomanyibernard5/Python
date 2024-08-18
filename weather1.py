import requests
from dotenv import load_dotenv
import os
from pprint import pprint
load_dotenv()

def get_weather():
    print("Getting current weather...🚀")
    try:
        city = input("\nPlease enter the city: ")

        api_key = os.getenv("API_KEY")
        request_url = f'https://api.openweathermap.org/data/2.5/weather?appid={api_key}&q={city}&units=imperial'

        weather_data = requests.get(request_url).json()
        
        if weather_data["cod"] != 200:
                raise ValueError(f"{city} is not a valid city.")

        print(f"\n***Current weather data at {city}***\n")
        print(f'Temperature: {weather_data["main"]["temp"]:.1f}°F')
        print(f'{weather_data["weather"][0]["description"].capitalize()} and feels like {weather_data["main"]["feels_like"]:.1f}°F\n')
        pprint(weather_data)

    except ValueError as error:
        print(f"\nRequest interrupted. ❌ {error}")
        get_weather() 

get_weather()
