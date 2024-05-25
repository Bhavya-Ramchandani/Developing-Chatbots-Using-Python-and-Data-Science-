import nltk
from nltk.tokenize import word_tokenize

messages = ["What's the weather like in Mumbai today?", "Do I need an umbrella in Delhi right now?"]
tokens = [word_tokenize(message.lower()) for message in messages]
import re

messages = ["What's the weather like in Mumbai today?", "Do I need an umbrella in Delhi right now?"]
date_pattern = r'\btoday\b|\btomorrow\b|\bnext week\b'

dates = []
for message in messages:
    match = re.search(date_pattern, message, re.IGNORECASE)
    if match:
        dates.append(match.group())
    else:
        dates.append("Date not specified")  # Or any other placeholder you prefer

print(dates)
date_pattern = r'\btoday\b|\btomorrow\b|\bnext week\b|\bnext month\b|on \bmonday\b|in \boctober\b'
import spacy

# Load the English NLP model
nlp = spacy.load("en_core_web_sm")

# Sample messages
messages = ["What's the weather like in Mumbai today?", "Do I need an umbrella in Delhi right now?"]

# Process messages and extract entities
for message in messages:
    doc = nlp(message)
    print([(ent.text, ent.label_) for ent in doc.ents])
import requests

def get_weather(location, date="today"):
    api_key = "your_api_key"
    # Construct the API URL
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        weather = data['weather'][0]['description']
        temperature = data['main']['temp']
        return f"The weather in {location} {date} is {weather} with a temperature of {temperature}°C."
    else:
        return "Weather data not available."

# Example usage with extracted entities
locations = [("Mumbai", "today"), ("Delhi", None)]
for location, date in locations:
    print(get_weather(location, date))
import requests

def get_weather(location, api_key):
    """ Fetch weather information from OpenWeatherMap API with detailed error handling. """
    url = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if 'weather' in data and 'main' in data:
            weather = data['weather'][0]['description']
            temp = data['main']['temp']
            return f"The weather in {location} is {weather} with a temperature of {temp}°C."
        else:
            return "Weather data format error."
    else:
        return f"Failed to retrieve weather data, status code: {response.status_code}, message: {response.text}"

# Example usage with enhanced error handling
api_key = "f03260150e0d585ff3d18c14ec9e9088"
locations = ["Mumbai", "Delhi", "A fictitious city"]
for location in locations:
    print(get_weather(location, api_key))

def get_extended_forecast(location, api_key):
    """ Fetch 5-day / 3-hour forecast data from OpenWeatherMap API. """
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={location}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        forecasts = []
        for item in data['list']:
            time = item['dt_txt']
            weather = item['weather'][0]['description']
            temp = item['main']['temp']
            forecasts.append(f"At {time}, expect {weather}, with a temperature of {temp}°C.")
        return "\n".join(forecasts)
    else:
        return "Failed to retrieve forecast data."

# Example usage
print(get_extended_forecast("Bengaluru", api_key))

def safe_get_weather(location, api_key):
    """ Safely fetch weather data with detailed error handling. """
    try:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"
        response = requests.get(url)
        response.raise_for_status()  # Will raise an HTTPError for bad requests (400 or 500)
        data = response.json()
        if "weather" in data and "main" in data:
            weather = data['weather'][0]['description']
            temp = data['main']['temp']
            return f"The weather in {location} is {weather} with a temperature of {temp}°C."
        else:
            return "Weather data format error."
    except requests.exceptions.HTTPError as err:
        return f"HTTP error occurred: {err}"
    except requests.exceptions.RequestException as err:
        return f"Error fetching data: {err}"

# Example usage
print(safe_get_weather("Kolkata", api_key))

def safe_get_weather(location, api_key):
    """ Safely fetch weather data with detailed error handling. """
    try:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"
        response = requests.get(url)
        response.raise_for_status()  # Will raise an HTTPError for bad requests (400 or 500)
        data = response.json()
        if "weather" in data and "main" in data:
            weather = data['weather'][0]['description']
            temp = data['main']['temp']
            return f"The weather in {location} is {weather} with a temperature of {temp}°C."
        else:
            return "Weather data format error."
    except requests.exceptions.HTTPError as err:
        return f"HTTP error occurred: {err}"
    except requests.exceptions.RequestException as err:
        return f"Error fetching data: {err}"

# Example usage
print(safe_get_weather("Bengaluru", api_key))

def safe_get_weather(location, api_key):
    """ Safely fetch weather data with detailed error handling. """
    try:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"
        response = requests.get(url)
        response.raise_for_status()  # Will raise an HTTPError for bad requests (400 or 500)
        data = response.json()
        if "weather" in data and "main" in data:
            weather = data['weather'][0]['description']
            temp = data['main']['temp']
            return f"The weather in {location} is {weather} with a temperature of {temp}°C."
        else:
            return "Weather data format error."
    except requests.exceptions.HTTPError as err:
        return f"HTTP error occurred: {err}"
    except requests.exceptions.RequestException as err:
        return f"Error fetching data: {err}"

# Example usage
print(safe_get_weather("Chennai", api_key))

def safe_get_weather(location, api_key):
    """ Safely fetch weather data with detailed error handling. """
    try:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"
        response = requests.get(url)
        response.raise_for_status()  # Will raise an HTTPError for bad requests (400 or 500)
        data = response.json()
        if "weather" in data and "main" in data:
            weather = data['weather'][0]['description']
            temp = data['main']['temp']
            return f"The weather in {location} is {weather} with a temperature of {temp}°C."
        else:
            return "Weather data format error."
    except requests.exceptions.HTTPError as err:
        return f"HTTP error occurred: {err}"
    except requests.exceptions.RequestException as err:
        return f"Error fetching data: {err}"

# Example usage
print(safe_get_weather("Hyderabad", api_key))

def safe_get_weather(location, api_key):
    """ Safely fetch weather data with detailed error handling. """
    try:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"
        response = requests.get(url)
        response.raise_for_status()  # Will raise an HTTPError for bad requests (400 or 500)
        data = response.json()
        if "weather" in data and "main" in data:
            weather = data['weather'][0]['description']
            temp = data['main']['temp']
            return f"The weather in {location} is {weather} with a temperature of {temp}°C."
        else:
            return "Weather data format error."
    except requests.exceptions.HTTPError as err:
        return f"HTTP error occurred: {err}"
    except requests.exceptions.RequestException as err:
        return f"Error fetching data: {err}"

# Example usage
print(safe_get_weather("Shimla", api_key))

def safe_get_weather(location, api_key):
    """ Safely fetch weather data with detailed error handling. """
    try:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"
        response = requests.get(url)
        response.raise_for_status()  # Will raise an HTTPError for bad requests (400 or 500)
        data = response.json()
        if "weather" in data and "main" in data:
            weather = data['weather'][0]['description']
            temp = data['main']['temp']
            return f"The weather in {location} is {weather} with a temperature of {temp}°C."
        else:
            return "Weather data format error."
    except requests.exceptions.HTTPError as err:
        return f"HTTP error occurred: {err}"
    except requests.exceptions.RequestException as err:
        return f"Error fetching data: {err}"

# Example usage
print(safe_get_weather("Goa", api_key))

def safe_get_weather(location, api_key):
    """ Safely fetch weather data with detailed error handling. """
    try:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"
        response = requests.get(url)
        response.raise_for_status()  # Will raise an HTTPError for bad requests (400 or 500)
        data = response.json()
        if "weather" in data and "main" in data:
            weather = data['weather'][0]['description']
            temp = data['main']['temp']
            return f"The weather in {location} is {weather} with a temperature of {temp}°C."
        else:
            return "Weather data format error."
    except requests.exceptions.HTTPError as err:
        return f"HTTP error occurred: {err}"
    except requests.exceptions.RequestException as err:
        return f"Error fetching data: {err}"

# Example usage
print(safe_get_weather("Jaipur", api_key))

def safe_get_weather(location, api_key):
    """ Safely fetch weather data with detailed error handling. """
    try:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"
        response = requests.get(url)
        response.raise_for_status()  # Will raise an HTTPError for bad requests (400 or 500)
        data = response.json()
        if "weather" in data and "main" in data:
            weather = data['weather'][0]['description']
            temp = data['main']['temp']
            return f"The weather in {location} is {weather} with a temperature of {temp}°C."
        else:
            return "Weather data format error."
    except requests.exceptions.HTTPError as err:
        return f"HTTP error occurred: {err}"
    except requests.exceptions.RequestException as err:
        return f"Error fetching data: {err}"

# Example usage
print(safe_get_weather("Pune", api_key))

def safe_get_weather(location, api_key):
    """ Safely fetch weather data with detailed error handling. """
    try:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"
        response = requests.get(url)
        response.raise_for_status()  # Will raise an HTTPError for bad requests (400 or 500)
        data = response.json()
        if "weather" in data and "main" in data:
            weather = data['weather'][0]['description']
            temp = data['main']['temp']
            return f"The weather in {location} is {weather} with a temperature of {temp}°C."
        else:
            return "Weather data format error."
    except requests.exceptions.HTTPError as err:
        return f"HTTP error occurred: {err}"
    except requests.exceptions.RequestException as err:
        return f"Error fetching data: {err}"

# Example usage
print(safe_get_weather("Ahmedabad", api_key))

def safe_get_weather(location, api_key):
    """ Safely fetch weather data with detailed error handling. """
    try:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"
        response = requests.get(url)
        response.raise_for_status()  # Will raise an HTTPError for bad requests (400 or 500)
        data = response.json()
        if "weather" in data and "main" in data:
            weather = data['weather'][0]['description']
            temp = data['main']['temp']
            return f"The weather in {location} is {weather} with a temperature of {temp}°C."
        else:
            return "Weather data format error."
    except requests.exceptions.HTTPError as err:
        return f"HTTP error occurred: {err}"
    except requests.exceptions.RequestException as err:
        return f"Error fetching data: {err}"

# Example usage
print(safe_get_weather("Varanasi", api_key))





