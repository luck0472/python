# define the temperature conversion functions

def celsius_to_fahrenheit(celsius):
    return celsius * 1.8 + 32   

def celsius_to_kelvin(celsius):
    return celsius + 273

def celsius_to_rankine(celsius):
    return celsius * 1.8 + 491.67

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) / 1.8

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit + 459.67) * 5 / 9    

def fahrenheit_to_rankine(fahrenheit):
    return fahrenheit + 459.67  

def kelvin_to_celsius(kelvin):
    return kelvin - 273

def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273) * 1.8 + 32

def kelvin_to_rankine(kelvin):
    return kelvin * 1.8 

def rankine_to_celsius(rankine):
    return (rankine - 491.67) / 1.8

def rankine_to_fahrenheit(rankine):
    return rankine - 459.67 

def rankine_to_kelvin(rankine):
    return rankine / 1.8    

# main loop for program 

while True:
        print("\nTemperature Conversion Menu")
        print("1. Celsius to Fahrenheit")
        print("2. Celsius to Kelvin")
        print("3. Celsius to Rankine")
        print("4. Fahrenheit to Celsius")
        print("5. Fahrenheit to Kelvin")
        print("6. Fahrenheit to Rankine")
        print("7. Kelvin to Celsius")
        print("8. Kelvin to Fahrenheit")
        print("9. Kelvin to Rankine")
        print("10. Rankine to Celsius")
        print("11. Rankine to Fahrenheit")
        print("12. Rankine to Kelvin")
        print("13. Exit")

        choice = input("Enter your choice (1-13): ")

        if choice == "1":
            celsius = float(input("Enter temperature in Celsius: "))
            fahrenheit = celsius_to_fahrenheit(celsius)
            print(f"{celsius} Celsius is equal to {fahrenheit} Fahrenheit.")
        elif choice == "2":
            celsius = float(input("Enter temperature in Celsius: "))
            kelvin = celsius_to_kelvin(celsius)
            print(f"{celsius} Celsius is equal to {kelvin} Kelvin.")
        elif choice == "3":
            celsius = float(input("Enter temperature in Celsius: "))
            rankine = celsius_to_rankine(celsius)
            print(f"{celsius} Celsius is equal to {rankine} Rankine.")
        elif choice == "4":
            fahrenheit = float(input("Enter temperature in Fahrenheit: "))
            celsius = fahrenheit_to_celsius(fahrenheit)
            print(f"{fahrenheit} Fahrenheit is equal to {celsius} Celsius.")
        elif choice == "5":
            fahrenheit = float(input("Enter temperature in Fahrenheit: "))
            kelvin = fahrenheit_to_kelvin(fahrenheit)
            print(f"{fahrenheit} Fahrenheit is equal to {kelvin} Kelvin.")
        elif choice == "6":
            fahrenheit = float(input("Enter temperature in Fahrenheit: "))
            rankine = fahrenheit_to_rankine(fahrenheit)
            print(f"{fahrenheit} Fahrenheit is equal to {rankine} Rankine.")
        elif choice == "7":
            kelvin = float(input("Enter temperature in Kelvin: "))
            celsius = kelvin_to_celsius(kelvin)
            print(f"{kelvin} Kelvin is equal to {celsius} Celsius.")
        elif choice == "8":
            kelvin = float(input("Enter temperature in Kelvin: "))
            fahrenheit = kelvin_to_fahrenheit(kelvin)
            print(f"{kelvin} Kelvin is equal to {fahrenheit} Fahrenheit.")
        elif choice == "9":
            kelvin = float(input("Enter temperature in Kelvin: "))
            rankine = kelvin_to_rankine(kelvin)
            print(f"{kelvin} Kelvin is equal to {rankine} Rankine.")
        elif choice == "10":
            rankine = float(input("Enter temperature in Rankine: "))
            celsius = rankine_to_celsius(rankine)
            print(f"{rankine} Rankine is equal to {celsius} Celsius.")
        elif choice == "11":
            rankine = float(input("Enter temperature in Rankine: "))
            fahrenheit = rankine_to_fahrenheit(rankine)
            print(f"{rankine} Rankine is equal to {fahrenheit} Fahrenheit.")
        elif choice == "12":
            rankine = float(input("Enter temperature in Rankine: "))
            kelvin = rankine_to_kelvin(rankine)
            print(f"{rankine} Rankine is equal to {kelvin} Kelvin.")
        elif choice == "13":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")