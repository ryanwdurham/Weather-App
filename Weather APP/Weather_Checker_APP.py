from flask import Flask, render_template, request
import requests

app = Flask(__name__)

GEOCODE_URL = "https://nominatim.openstreetmap.org/search"
FALLBACK_GEOCODE = "https://geocoding-api.open-meteo.com/v1/search"
WEATHER_URL = "https://api.open-meteo.com/v1/forecast"
HEADERS = {"User-Agent": "WeatherChecker/2.0 (example@example.com)"}
REQUEST_TIMEOUT = 10

# Map weather codes → description + Unicode icon
WEATHER_CODE_MAP = {
    0: ("Clear sky", "☀️"), 1: ("Mainly clear", "🌤"), 2: ("Partly cloudy", "⛅"), 3: ("Overcast", "☁️"),
    45: ("Fog", "🌫"), 48: ("Rime fog", "🌫"), 51: ("Light drizzle", "🌦"), 53: ("Moderate drizzle", "🌦"),
    55: ("Dense drizzle", "🌧"), 61: ("Slight rain", "🌧"), 63: ("Moderate rain", "🌧"), 65: ("Heavy rain", "🌧"),
    71: ("Slight snow", "🌨"), 73: ("Moderate snow", "🌨"), 75: ("Heavy snow", "❄️"),
    80: ("Slight rain showers", "🌦"), 81: ("Moderate rain showers", "🌦"), 82: ("Violent rain showers", "⛈"),
    95: ("Thunderstorm", "⛈"), 96: ("Thunderstorm w/ hail", "⛈"), 99: ("Severe thunderstorm w/ hail", "⛈")
}

def get_coordinates(city):
    try:
        params = {"q": city, "format": "json", "limit": 1}
        resp = requests.get(GEOCODE_URL, params=params, headers=HEADERS, timeout=REQUEST_TIMEOUT)
        data = resp.json()
        if data:
            d = data[0]
            return float(d["lat"]), float(d["lon"]), d.get("display_name", city)
    except:
        pass
    try:
        params2 = {"name": city, "count": 1}
        resp2 = requests.get(FALLBACK_GEOCODE, params=params2, timeout=REQUEST_TIMEOUT)
        res = resp2.json().get("results")
        if res:
            r = res[0]
            return float(r["latitude"]), float(r["longitude"]), r.get("name", city)
    except:
        pass
    return None

def get_weather(lat, lon):
    params = {
        "latitude": lat, "longitude": lon,
        "current_weather": True, "timezone": "auto",
        "daily": "temperature_2m_max,temperature_2m_min,weathercode"
    }
    data_c = requests.get(WEATHER_URL, params=params, timeout=REQUEST_TIMEOUT).json()
    params["temperature_unit"] = "fahrenheit"
    data_f = requests.get(WEATHER_URL, params=params, timeout=REQUEST_TIMEOUT).json()
    return data_c, data_f

@app.route("/", methods=["GET", "POST"])
def index():
    weather_info = None
    error = None

    if request.method == "POST":
        city = request.form.get("city")
        coords = get_coordinates(city)

        if not coords:
            error = "❌ Could not find that city."
        else:
            lat, lon, place = coords
            data_c, data_f = get_weather(lat, lon)
            if not data_c or not data_f:
                error = "❌ Weather data unavailable."
            else:
                current_c = data_c["current_weather"]
                current_f = data_f["current_weather"]
                daily_c = data_c["daily"]
                daily_f = data_f["daily"]

                forecast = []
                for i in range(7):
                    code = daily_c["weathercode"][i]
                    desc, icon = WEATHER_CODE_MAP.get(code, ("Unknown", "❓"))
                    forecast.append({
                        "date": daily_c["time"][i],
                        "desc": desc,
                        "icon": icon,
                        "tmin_c": daily_c["temperature_2m_min"][i],
                        "tmax_c": daily_c["temperature_2m_max"][i],
                        "tmin_f": daily_f["temperature_2m_min"][i],
                        "tmax_f": daily_f["temperature_2m_max"][i],
                    })

                code = current_c["weathercode"]
                desc, icon = WEATHER_CODE_MAP.get(code, ("Unknown", "❓"))
                weather_info = {
                    "place": place,
                    "temp_c": current_c["temperature"],
                    "temp_f": current_f["temperature"],
                    "windspeed": current_c["windspeed"],
                    "winddir": current_c["winddirection"],
                    "condition": desc,
                    "icon": icon,
                    "forecast": forecast
                }

    return render_template("index.html", weather=weather_info, error=error)

if __name__ == "__main__":
    app.run(debug=True)
