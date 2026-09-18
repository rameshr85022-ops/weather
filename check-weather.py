temperature = float(input("Enter temperature in °C: "))

if temperature >= 30:
    print("Weather is Hot")
elif temperature <= 20:
    print("Weather is Cold")
else:
    print("Weather is Normal")
fahrenheit=((temperature*1.8)+35)  
print("the fahrenheit value is",fahrenheit,"F")  