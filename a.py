import requests
import json

HER_CODES = {
    '200': '⛈ ',
    '201': '⛈ ',
    '202': '⛈ ',
    '210': '⛈ ',
    '211': '🌩 ',
    '212': '🌩 ',
    '221': '🌩 ',
    '230': '⛈ ',
    '231': '⛈ ',
    '232': '⛈ ',
    '300': '🌧 ',
    '301': '🌧 ',
    '302': '🌧 ',
    '310': '🌧 ',
    '311': '🌧 ',
    '312': '🌧 ',
    '313': '🌧 ',
    '314': '🌧 ',
    '321': '🌧 ',
    '500': '🌧 ',
    '501': '🌧 ',
    '502': '🌧 ',
    '503': '🌧 ',
    '504': '🌧 ',
    '511': '🌧 ',
    '520': '🌧 ',
    '521': '🌧 ',
    '522': '🌧 ',
    '531': '🌧 ',
    '600': '🌨 ',
    '601': '🌨 ',
    '602': '🌨 ',
    '611': '🌨 ',
    '612': '🌨 ',
    '613': '🌨 ',
    '615': '🌨 ',
    '616': '🌨 ',
    '620': '🌨 ',
    '621': '🌨 ',
    '622': '🌨 ',
    '701': '🌫 ',
    '711': '🌫 ',
    '721': '🌫 ',
    '731': '🌫 ',
    '741': '🌫 ',
    '751': '🌫 ',
    '761': '🌫 ',
    '762': '🌫 ',
    '771': '🌬 ',
    '781': '🌪 ',
    '800': ' ',
    '801': '🌤 ',
    '802': '🌥 ',
    '803': '🌥 ',
    '804': '☁️ '
}

def get_weather(city):
    api_key = "0893defca21907657083a55440bd9f71"  # Replace with your actual API key
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "q=" + city + "&appid=" + api_key + "&units=metric"

    response = requests.get(complete_url)
    print(response.status_code)
    print(response.text)
    data = response.json()

    if data["cod"] != "404":
        main = data["main"]
        weather = data["weather"][0]
        temperature = round(main["temp"])  # Round temperature to nearest integer
        description = weather["description"]
        weather_code = str(data["weather"][0]["id"])

        weather_info = {
            "text": f"{city}: {temperature}°C, {description} {HER_CODES.get(weather_code, '')}",
            "tooltip": f"City: {city}\nTemperature: {temperature}°C\nDescription: {description}"
        }

        with open("/home/eko/temperature.json", "w") as file:
            json.dump(weather_info, file)
    else:
        with open("/home/eko/temperature.json", "w") as file:
            json.dump({"text": "City not found."}, file)

if __name__ == "__main__":
    city_name = "Erzurum"
    get_weather(city_name)
