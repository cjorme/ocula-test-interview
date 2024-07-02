import pytest
import pprint
from resources.openweather_api import get_weather_by_city

# Test function() to validate the presence of specified keys in the JSON response.
def test_get_weather_by_city():
    city = "Belfast"
    weather_api_key = "08cde2ac41432dc445bb68b94c84edef"
    response, data_set = get_weather_by_city(city, weather_api_key)
    pprint.pprint(data_set)
    
# Verify the minimum, maximum, temperature, and humidity values exist in correct schema elements

    content_type = response.headers.get("Content-Type")
    main = data_set["main"]

    assert response.status_code == 200, "Unexpected Status Code: " + str(response.status_code)
    assert content_type == "application/json; charset=utf-8", "Unexpected Content-Type: " + content_type
    
    # Check if the "main" key is present in the JSON response - holds relevant Temperature data
    assert "main" in data_set, "Expected 'main' key not found in the JSON response"
    
    if "temp_min" in main and "temp_max" in main and "temp" in main and "humidity" in main:
        print(f"Minimum Temperature: {main['temp_min']}")
        print(f"Maximum Temperature: {main['temp_max']}")
        print(f"Temperature: {main['temp']}")
        print(f"Humidity: {main['humidity']}")
    else:
        raise ValueError("One or more expected keys are missing from within 'main'")
    
# alternative assertions for testing above
    # assert response.status_code == 200, "Unexpected Status Code: " + str(response.status_code)
    # assert content_type == "application/json; charset=utf-8", "Unexpected Content-Type: " + content_type
    # assert "main" in data_set, "Expected 'main' key not found in the JSON response"
    # assert "temp_min" in main, "Expected 'temp_min' key not found in the 'main' section"
    # assert "temp_max" in main, "Expected 'temp_max' key not found in the 'main' section"
    # assert "temp" in main, "Expected 'temp' key not found in the 'main' section"
    # assert "humidity" in main, "Expected 'humidity' key not found in the 'main' section"
    

# removed as only running via pytest, rather than standalone script
# if __name__ == "__main__":
#     # Call the test function when the script is executed manually
#     test_get_weather_by_city()