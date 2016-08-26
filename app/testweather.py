import pyowm

#todo, hide key in keystore

owm = pyowm.OWM('73577fe4d4c5426ca395f5a679af2412')  # You MUST provide a valid API key

# You have a pro subscription? Use:
# owm = pyowm.OWM(API_key='your-API-key', subscription_type='pro')

# Will it be sunny tomorrow at this time in Milan (Italy) ?
forecast = owm.daily_forecast("Milan,it")
tomorrow = pyowm.timeutils.tomorrow()
forecast.will_be_sunny_at(tomorrow)  # Always True in Italy, right? ;-)

# Search for current weather in London (UK)
observation = owm.weather_at_place('Utrecht,nl')
w = observation.get_weather()
print(w)
w.get_temperature(unit='celsius')
w.get_detailed_status()
# status (cloudy); Hi , Lo, wind.

t = w.get_temperature(unit='celsius')
t.get('temp_min')
t.get('temp_max')
display = "T:" + '{:0.0f}'.format(t.get('temp_min')) + "-" + '{:0.0f}'.format(t.get('temp_max')) +" W:" + '{:0.0f}'.format(w.get_wind()['speed']) + " " + w.get_detailed_status()
# add wind

print(display)

