from ss import *
import requests

api_address = f"https://api.openweathermap.org/data/2.5/weather?q=Delhi&appid={key2}"  # Assuming key2 is your API key
json_data = requests.get(api_address).json()

def temp():
    temperature = round(json_data["main"]["temp"] - 273.15, 1)  # Convert temperature from Kelvin to Celsius
    return temperature

def des():
    description = json_data["weather"][0]["description"]
    return description


# Print temperature and description
# temperature = temp()
# print(f"Temperature: {temperature} °C")
#
# description = des()
# print(f"Weather Description: {description}")

