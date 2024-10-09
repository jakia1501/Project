# UnitConverter.py

# Functions to handle various conversions

# Length conversions
def meters_to_feet(meters):
    return meters * 3.28084


def feet_to_meters(feet):
    return feet / 3.28084


def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


def kilograms_to_pounds(kilograms):
    return kilograms * 2.20462


def pounds_to_kilograms(pounds):
    return pounds / 2.20462


def main():
    print("Welcome to the Unit Converter!")


    print("Choose a conversion type:")
    print("1. Length (meters <-> feet)")
    print("2. Temperature (Celsius <-> Fahrenheit)")
    print("3. Weight (kilograms <-> pounds)")

    try:
        choice = int(input("Enter your choice (1/2/3): "))

        if choice == 1:

            length = float(input("Enter the length value: "))
            unit = input("Is the value in meters (m) or feet (f)? ").lower()

            if unit == 'm':
                result = meters_to_feet(length)
                print(f"{length} meters is {result:.2f} feet.")
            elif unit == 'f':
                result = feet_to_meters(length)
                print(f"{length} feet is {result:.2f} meters.")
            else:
                print("Invalid unit! Please enter 'm' for meters or 'f' for feet.")

        elif choice == 2:

            temp = float(input("Enter the temperature value: "))
            unit = input("Is the value in Celsius (c) or Fahrenheit (f)? ").lower()

            if unit == 'c':
                result = celsius_to_fahrenheit(temp)
                print(f"{temp} Celsius is {result:.2f} Fahrenheit.")
            elif unit == 'f':
                result = fahrenheit_to_celsius(temp)
                print(f"{temp} Fahrenheit is {result:.2f} Celsius.")
            else:
                print("Invalid unit! Please enter 'c' for Celsius or 'f' for Fahrenheit.")

        elif choice == 3:

            weight = float(input("Enter the weight value: "))
            unit = input("Is the value in kilograms (kg) or pounds (lb)? ").lower()

            if unit == 'kg':
                result = kilograms_to_pounds(weight)
                print(f"{weight} kilograms is {result:.2f} pounds.")
            elif unit == 'lb':
                result = pounds_to_kilograms(weight)
                print(f"{weight} pounds is {result:.2f} kilograms.")
            else:
                print("Invalid unit! Please enter 'kg' for kilograms or 'lb' for pounds.")

        else:
            print("Invalid choice! Please enter 1, 2, or 3.")

    except ValueError:
        print("Invalid input! Please enter a valid number.")


if __name__ == "__main__":
    main()
