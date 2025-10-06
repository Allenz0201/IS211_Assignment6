# conversions.py

def convertCelsiusToKelvin(celsius):
    """Takes in a float representing a Celsius measurement, and returns that temperature converted into Kelvins"""
    kelvins = float(celsius) + 273.15
    return kelvins

def convertCelsiusToFahrenheit(celsius):
    """Takes in a float representing a Celsius measurement, and returns that temperature converted into Fahrenheit"""
    fahrenheit = float(celsius) * 9.0 / 5.0 + 32.0
    return fahrenheit

def convertFahrenheitToCelsius(fahrenheit):
    """Takes in a float representing a Fahrenheit measurement, and returns that temperature converted into Celsius"""
    celsius = (float(fahrenheit) - 32.0) * 5.0 / 9.0
    return celsius

def convertFahrenheitToKelvin(fahrenheit):
    """Takes in a float representing a Fahrenheit measurement, and returns that temperature converted into Kelvins"""
    kelvins = (float(fahrenheit) - 32.0) * 5.0 / 9.0 + 273.15
    return kelvins

def convertKelvinToCelsius(kelvin):
    """Takes in a float representing a Kelvin measurement, and returns that temperature converted into Celsius"""
    celsius = float(kelvin) - 273.15
    return celsius

def convertKelvinToFahrenheit(kelvin):
    """Takes in a float representing a Kelvin measurement, and returns that temperature converted into Fahrenheit"""
    fahrenheit = (float(kelvin) - 273.15) * 9.0 / 5.0 + 32.0
    return fahrenheit
