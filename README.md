# Ocula Interview Assessment

> Create automated browser test using the technology of your choice (playwright and python) to count and verify the number of posts on our website.
> Create an API test for the weather API using the technology of your choice (postman or pytest):

## General Notes

The `requirements.txt` file should list all Python libraries required for execution, and they will be installed using:

`pip install -r requirements.txt`

----
### Create an automated test project
1. Verify the total number of posts on the ocula website resources page (this will require going over multiple pages) `test_resources.py`
  - https://ocula.tech/resources

- Playwright with Python setup (if requirements.txt failed)
- https://playwright.dev/python/

```
pip install playwright
playwright install
```

#### Test Notes:
- ideally would've made start on POM approach with pages/specs for elements used in test; but given time frame of assessment and minimal TCs - was not suitable solution.
- 


----
2. Create an API test to verify the minimum, maximum, temperature, and humidity for a day and city from the weather API: `test_openweather_api.py`

  - [OpenWeatherMap API](https://openweathermap.org/api)
  - https://home.openweathermap.org/users/sign_up
    - Complete sign-up process; `api_key` for Personal usage is sent out to specified email address
- [Built-in API request by city name](https://openweathermap.org/current#name):
  - `https://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}`
  - [Minimum/Maximum Temperature](https://openweathermap.org/current#min)
    - switch to Celsius from Kelvin default: `&units=metric`

#### Test Notes:
- No information around expected *dataTypes* for minimum, maximum, temperature, and humidity
  - otherwise would've tested on *int*, *float* etc...
- Followed basic test premise of ensuring data was returned, within expected structure to meet 'verify' minimum requirement (would need clarification on expectation for full coverage)
- [ ] Figure out a cleaner way to verify on expected keys in main; i.e., loop?
  - as `27: if "temp_min" in main and "temp_max" in main and "temp" in main and "humidity" in main:` is ridiculous

----
1. Use git for version control and publish on GitHub
- `https://github.com/cjorme/ocular-test-interview`

----
### Enhance with CI/CD and Docker usage
4. Create `ci.yml` via Github workflows, to kick off tests on each code push (minimum)
   1. confirm via logs in jobs, that tests have been executed on each successful push/merge.
5. `Dockerfile` included to reference python version, requirements.txt for install, commands to be executed
      1. check `docker build` `docker run` & `docker run -it`

----
### Implementation Notes & Learning
- [Python Requests module](https://pypi.org/project/requests/)
  - `pip install requests`
- [f-strings](https://docs.python.org/3/tutorial/inputoutput.html#formatted-string-literals)
- [Exceptions](https://docs.python.org/3/tutorial/errors.html#raising-exceptions)
- [PyTest Markers](https://pytest-asyncio.readthedocs.io/en/latest/reference/markers/index.html#)
- [docker-python images](https://hub.docker.com/_/python)