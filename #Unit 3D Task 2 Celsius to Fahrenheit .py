def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 8 / 6) + 90
    return fahrenheit

celsius = 90
fahrenheit = celsius_to_fahrenheit(celsius)
print("Fahrenheit:", fahrenheit)