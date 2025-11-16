# 🌤️ Weather Checker

A clean and simple Flask web application that provides current weather conditions and a 7-day forecast for any city worldwide. Features dual temperature units (Celsius/Fahrenheit) and intuitive weather icons.

![Python Version](https://img.shields.io/badge/python-3.7%2B-blue)
![Flask](https://img.shields.io/badge/flask-2.0%2B-green)


## ✨ Features

- 🌍 **Global City Search**: Look up weather for any city worldwide
- 🌡️ **Dual Temperature Display**: View temperatures in both Celsius and Fahrenheit
- 📅 **7-Day Forecast**: Plan ahead with a week's worth of weather predictions
- 🎨 **Weather Icons**: Visual representation of weather conditions using emojis
- 💨 **Wind Information**: Current wind speed and direction
- 🔄 **Fallback Geocoding**: Multiple geocoding services for reliable city lookup
- 📱 **Responsive Design**: Works seamlessly on desktop and mobile devices
- 🆓 **No API Keys Required**: Uses free, open-source APIs

## 🎯 Weather Information Displayed

### Current Weather
- Temperature (°C and °F)
- Weather condition with icon
- Wind speed and direction
- Location name

### 7-Day Forecast
- Daily high and low temperatures
- Weather conditions for each day
- Visual weather icons
- Date information


Watch a demo in action here:  https://www.loom.com/share/e75849b424f34593ae142b25f9eafa70


## 📋 Requirements

- Python 3.7 or higher
- Flask 2.0+
- requests library

## 🚀 Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/weather-checker.git
cd weather-checker
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

**requirements.txt:**
```txt
Flask>=2.0.0
requests>=2.26.0
```

## 💻 Usage

### Running the Application

1. Start the Flask development server:
```bash
python app.py
```

2. Open your web browser and navigate to:
```
http://127.0.0.1:5000/
```

3. Enter a city name and click "Get Weather" to see results!

### Production Deployment

For production environments, use a WSGI server like Gunicorn:

```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:8000 app:app
```


## 🔧 How It Works

### APIs Used

The application uses three free, open-source APIs:

1. **OpenStreetMap Nominatim** (Primary Geocoding)
   - Converts city names to coordinates
   - URL: https://nominatim.openstreetmap.org/

2. **Open-Meteo Geocoding** (Fallback)
   - Backup geocoding service
   - URL: https://geocoding-api.open-meteo.com/

3. **Open-Meteo Weather API**
   - Provides current weather and forecasts
   - URL: https://api.open-meteo.com/
   - No API key required!

### Weather Codes

The app translates numeric weather codes into human-readable descriptions:

| Code | Condition | Icon |
|------|-----------|------|
| 0 | Clear sky | ☀️ |
| 1 | Mainly clear | 🌤 |
| 2 | Partly cloudy | ⛅ |
| 3 | Overcast | ☁️ |
| 45, 48 | Fog | 🌫 |
| 51-55 | Drizzle | 🌦 |
| 61-65 | Rain | 🌧 |
| 71-75 | Snow | 🌨❄️ |
| 80-82 | Rain showers | 🌦⛈ |
| 95-99 | Thunderstorm | ⛈ |

## 🛠️ Configuration

### Timeout Settings

Adjust API request timeout (default: 10 seconds):
```python
REQUEST_TIMEOUT = 15  # Increase for slower connections
```

### Adding More Weather Codes

Extend the `WEATHER_CODE_MAP` dictionary to add custom weather conditions:
```python
WEATHER_CODE_MAP = {
    # ... existing codes
    100: ("Custom condition", "🌈"),
}
```

## 🐛 Troubleshooting

### Common Issues

**Issue**: City not found
```
Solution: Try variations of the city name:
- "New York" vs "New York City"
- Include country: "Paris, France" vs "Paris, Texas"
- Use full official names
```

**Issue**: Timeout errors
```
Solution: Increase REQUEST_TIMEOUT value or check internet connection
```

**Issue**: Template not found
```
Solution: Ensure index.html is in a 'templates' folder in the same directory as app.py
```

**Issue**: Port 5000 already in use
```
Solution: Change the port:
app.run(debug=True, port=5001)
```

## 📊 Example Searches

Try these cities to test the application:
- New York
- London
- Tokyo
- Sydney
- Paris
- Mumbai
- São Paulo
- Cairo


## 🎨 Customization

### Adding Custom Styling

The HTML template can be customized with your own CSS. Consider adding:
- Custom color schemes
- Animation effects
- Chart visualizations
- Background images based on weather conditions

### Database Integration

Store search history or favorite locations:
```python
from flask_sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///weather.db'
db = SQLAlchemy(app)

class SearchHistory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String(100))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
```


## 📄 License


## 🙏 Acknowledgments

- [Open-Meteo](https://open-meteo.com/) - Free weather API
- [OpenStreetMap Nominatim](https://nominatim.openstreetmap.org/) - Geocoding service
- Flask community for excellent documentation
- Weather enthusiasts worldwide 🌍



## 🌟 Star This Repo

If you find this project useful, please consider giving it a star! ⭐

---
