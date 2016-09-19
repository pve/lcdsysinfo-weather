import pyowm, os
from pyowm import timeutils

#todo, hide key in keystore
owmkey = os.getenv('OWMKEY', 'novalidkey' )

owm = pyowm.OWM('73577fe4d4c5426ca395f5a679af2412')  # You MUST provide a valid API key
#owm = pyowm.OWM(owmkey)
#owm.is_API_online()

# Search for current weather 
observation = owm.weather_at_place('Utrecht,nl')
observation = owm.weather_at_id(2745912) #Utrecht
forecast = owm.daily_forecast("Utrecht,nl")
# fo = forecast.get_weather_at(timeutils.next_three_hours())
# this is not always in the forecast

wo = observation.get_weather()

def weatherline(w):
#forecast and observation don't have same min/max
  t = w.get_temperature(unit='celsius')
  tmin = t.get('temp_min')
  tmin = tmin if tmin != None else t.get('min')
  tmax = t.get('temp_max')
  tmax = tmax if tmax != None else t.get('max')
  display = "T:" + '{:0.0f}'.format(tmin) + "-" + '{:0.0f}'.format(tmax)
  display += " W:" + '{:0.0f}'.format(w.get_wind()['speed']) + " " + w.get_detailed_status()
  return display

#print(weatherline(wo))
def observe():
    return weatherline(wo)

#print(weatherline(fo))

