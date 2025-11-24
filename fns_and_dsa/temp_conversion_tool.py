# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5


def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius using the global factor"""
    global FAHRENHEIT_TO_CELSIUS_FACTOR  # explicitly accessing global variable
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR


def convert_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit using the global factor"""
    global CELSIUS_TO_FAHRENHEIT_FACTOR  # explicitly accessing global variable
    return celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32


def main():
    # Input validation loop for temperature
    while True:
        temp_input = input("Enter the temperature to convert: ").strip()
        try:
            temperature = float(temp_input)
            break
        except ValueError:
            print("Invalid temperature. Please enter a numeric value.")

    # Input validation loop for unit
    while True:
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
        if unit in ("C", "F"):
            break
        else:
            print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

    # Conversion based on unit
    if unit == "C":
        converted = convert_to_fahrenheit(temperature)
        print(f"{temperature}°C is {converted}°F")
    else:  # unit == "F"
        converted = convert_to_celsius(temperature)
        print(f"{temperature}°F is {converted}°C")


if __name__ == "__main__":
    main()
