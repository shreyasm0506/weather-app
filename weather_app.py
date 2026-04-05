import requests
city=input("Enter the name of the city: ")

api_key="your_api_key_here"
url=f"https://api.dd1bopenweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
response = requests.get(url)
data=response.json()

if data["cod"]==200:
    temp=data["main"]["temp"]
    feels_like=data["main"]["feels_like"]
    humidity = data["main"]["humidity"]
    description = data["weather"][0]["description"]
    country = data["sys"]["country"]
    wind=data["wind"]["speed"]

    print(f"\nWeather in {city.title()}, {country}:")
    print(f"Temperature  : {temp}°C")
    print(f"Feels like   : {feels_like}°C")
    print(f"Humidity     : {humidity}%")
    print(f"Condition    : {description.title()}")
    print(f"Wind         : {wind} m/s")
else:
    print("City not found. Please check the name and try again.")