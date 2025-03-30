temperature = 35
cloudy = False
humidity = 60
wind_speed = 15
raining = True

a = temperature > 30 and not cloudy  # True
b = humidity < 50 or wind_speed > 10  # True 
c = raining == True and wind_speed < 20  # True 
d = temperature <= 25 or cloudy  # False 
e = not (humidity > 70 and raining)  # True 

print(a, b, c, d, e)