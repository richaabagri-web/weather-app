import requests

class WeatherApp:
    def __init__(self, api_key):
        self.api_key = api_key

    def get_weather(self, city):
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={self.api_key}&units=metric"
        response = requests.get(url)
        data = response.json()

        if data["cod"] == 401:
            print("❌ API key not activated yet!")
        elif data["cod"] == "404":
            print("❌ City not found!")
        else:
            temp = data["main"]["temp"]
            condition = data["weather"][0]["description"]
            humidity = data["main"]["humidity"]
            feels_like = data["main"]["feels_like"]
            country = data["sys"]["country"]

            print(f"🌍 City: {city}, {country}")
            print(f"🌡️ Temperature: {temp}°C")
            print(f"🥶 Feels like: {feels_like}°C")
            print(f"🌤️ Condition: {condition}")
            print(f"💧 Humidity: {humidity}%")

api_key = "dbbc6926ef42c6a33d06ec61fd12823e"
app = WeatherApp(api_key)

while True:
    city = input("\n🌍 Enter a city name (or 'quit' to exit): ")
    if city.lower() == "quit":
        print("👋 Goodbye!")
        break
    app.get_weather(city)
   