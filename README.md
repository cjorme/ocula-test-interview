# Ocula API Test

```Create automated browser test using the technology of your choice (playwright and python) to count and verify the number of posts on our website. Create an API test for the weather APIusing the technology of your choice (postman or pytest):```


### Create an automated test project
1. Verify the total number of posts on the ocula website resources page (this will require going over multiple pages)
  - https://ocula.tech/resources

- Playwright with Python setup
```
pip install playwright
playwright install
```





----
1. Create an API test to verify the minimum, maximum, temperature, and humidity for a day and city from the weather API:
  - http://openweathermap.org/api

```https://home.openweathermap.org/users/sign_up```

----
2. Use git for version control and publish on GitHub


### Enhance with CI/CD and Docker usage
4. a

----
### Notes
- [Python Requests module](https://pypi.org/project/requests/)
  - `pip install requests`
- [f-strings](https://docs.python.org/3/tutorial/inputoutput.html#formatted-string-literals)
- [Exceptions](https://docs.python.org/3/tutorial/errors.html#raising-exceptions)

- [OpenWeatherMap API](https://openweathermap.org/api)
- [Built-in API request by city name](https://openweathermap.org/current#name):
  - `https://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}`
  - [Minimum/Maximum Temperature](https://openweathermap.org/current#min)
    - switch to Celsius from Kelvin default: `&units=metric`


### Sample JSON Response - Belfast (Metric)
- [pprint](https://docs.python.org/3/library/pprint.html)
```
{
    "coord": {
        "lon": -5.9333,
        "lat": 54.5833
    },
    "weather": [
        {
            "id": 804,
            "main": "Clouds",
            "description": "overcast clouds",
            "icon": "04d"
        }
    ],
    "base": "stations",
    "main": {
        "temp": 13.54,
        "feels_like": 13.56,
        "temp_min": 13.54,
        "temp_max": 13.6,
        "pressure": 1019,
        "humidity": 100,
        "sea_level": 1019,
        "grnd_level": 1007
    },
    "visibility": 10000,
    "wind": {
        "speed": 1.59,
        "deg": 299,
        "gust": 2.06
    },
    "clouds": {
        "all": 100
    },
    "dt": 1719305417,
    "sys": {
        "type": 2,
        "id": 2008547,
        "country": "GB",
        "sunrise": 1719287319,
        "sunset": 1719349444
    },
    "timezone": 3600,
    "id": 2655984,
    "name": "Belfast",
    "cod": 200
}
```