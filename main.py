import requests
from config import API_KEY, BASE_URL

def get_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    response = requests.get(BASE_URL, params=params)

    if response.status_code == 200:
        try:
            data = response.json()
        except Exception:
            print("❌ Invalid response from API:")
            print(response.text)
            return

        weather = data["weather"][0]["description"].title()
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]

        print(f"\n🌍 Weather in {city.title()}")
        print(f"🌡 Temperature: {temp}°C")
        print(f"🌤 Condition: {weather}")
        print(f"💧 Humidity: {humidity}%")
        print(f"🌬 Wind Speed: {wind_speed} m/s")
    else:
        print("❌ Error:", response.status_code)
        print(response.text)

if __name__ == "__main__":
    city_name = input("Enter city name: ")
    get_weather(city_name)
