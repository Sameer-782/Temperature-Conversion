# Convert Fahrenheit to Celsius
print("This program converts temperatures Fahrenheit to Celsius!")
original_temperature = float(input("Enter the temperature in Fahrenheit: "))

# Conversion formula
converted_temperature = (original_temperature - 32) * 5/9
print(f"{original_temperature} degrees Fahrenheit is equal to {converted_temperature:.2f} degrees Celsius.")