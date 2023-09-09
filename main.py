import requests
API_KEY = "66b0bb2901e1ff5506e06e4555609766"
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"

weather_params ={
    "lat": 14.59,
    "lon": 120.98,
    "appid": API_KEY
}

will_rain = False

response = requests.get(OWM_Endpoint, params=weather_params)
data = response.json()
data_weather = data["list"]
# print(data["list"][2]["weather"][0]["id"])
weather_slice = data_weather[:4]
# print(weather_slice)
for i in range(len(weather_slice)):
    condition = weather_slice[i]["weather"][0]["id"]
    if int(condition) <= 500:
        will_rain = True
if will_rain:
    print("Bring Umbrella")