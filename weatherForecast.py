import pyowm
dic = {} 
owm = pyowm.OWM('Your API Key')  # You MUST provide a valid API key
 
# Search for current weather in London (Great Britain)
observation = owm.weather_manager()
dd = observation.weather_at_place('Montpellier , FR')
xx = dd.weather
print(xx)
dic =  xx.temperature(unit='celsius')  
 
print('La temperature est: ', xx.temperature(unit='celsius'))
for key,value in dic.items():
    if key == 'temp':
        print(value)
