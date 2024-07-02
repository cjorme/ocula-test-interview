import requests
import pprint

# Test function() to GET response of the OpenWeatherMap API for specified city and validate the presence of specified keys in the JSON response.

def test_weather_api():
    city = "Belfast"
    weather_api_key = "08cde2ac41432dc445bb68b94c84edef"
    units = "metric"
    weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_api_key}&units={units}"
    
    response = requests.get(weather_url)
    data_set = response.json()
    pprint.pprint(data_set)
    
# Verify the minimum, maximum, temperature, and humidity values exist in correct schema elements

    content_type = response.headers.get("Content-Type")
    main = data_set["main"]

    assert response.status_code == 200, "Unexpected Status Code: " + str(response.status_code)
    assert content_type == "application/json; charset=utf-8", "Unexpected Content-Type: " + content_type
    
    # Check if the "main" key is present in the JSON response - holds relevant Temperature data
    assert "main" in data_set, "Expected 'main' key not found in the JSON response"
    
    if "temp_min" in main and "temp_max" in main and "temp" in main and "humidity" in main:
        print(f"\n\n\nMinimum Temperature: {main['temp_min']}")
        print(f"Maximum Temperature: {main['temp_max']}")
        print(f"Temperature: {main['temp']}")
        print(f"Humidity: {main['humidity']}")
    else:
        raise ValueError("One or more expected keys are missing from within 'main'")
    

# Call the test function when the script is executed manually via Python
if __name__ == "__main__":
    test_weather_api()