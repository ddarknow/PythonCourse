# Presentation 8.1:

from pyowm import OWM

owm = OWM('1a1e11d9f872bfe18a6f2008332a1c5d')

mgr = owm.weather_manager()
observation = mgr.weather_at_place('Ternopil,UA')
w = observation.weather
print(w)

# Weather details
print(w.wind())
print(w.humidity)
print(w.temperature('celsius'))