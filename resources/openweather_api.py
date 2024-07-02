import requests
import pprint

# Function() for GET response of the OpenWeatherMap API for specified city, returnign data_set for future usage.

def get_weather_by_city(city, weather_api_key, units = "metric"):
    weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_api_key}&units={units}"
    response = requests.get(weather_url)
    data_set = response.json()
    pprint.pprint(data_set)
    return response, data_set
    
    #debugging purposes - \n etc...
def print_weather_ocula(data_set):
    main = data_set["main"]
    print(f"\n\n\nMinimum Temperature: {main['temp_min']}")
    print(f"Maximum Temperature: {main['temp_max']}")
    print(f"Temperature: {main['temp']}")
    print(f"Humidity: {main['humidity']}\n\n\n")    

if __name__ == "__main__":
    # Call the test function when the script is executed manually
    # print data to terminal from both above functions
    city = "Belfast"
    weather_api_key = "08cde2ac41432dc445bb68b94c84edef"
    get_weather_by_city(city, weather_api_key)
    response, data_set = get_weather_by_city(city, weather_api_key)
    print_weather_ocula(data_set)