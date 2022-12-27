# python program to convert temperature to and from Celsius to Fahrenheit.
print("--Celsius - Fahrenheit--")
a = float(input("Enter the Temprature : "))
print("Temperature in Celcius = ",a,"Degree")
farh = (a * 1.8) + 32
print("Temperature in Fahrenheit = ",farh,"Degree")

print("\n")

print("--Fahrenheit - Celsius--")
b = float(input("Enter the Temprature : "))
print("Temperature in Fahrenheit = ",b,"Degree")
cel = ((b - 32) * 5) / 9
print("Temperature in Celcius = ",cel,"Degree")