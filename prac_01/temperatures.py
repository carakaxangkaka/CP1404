MENU = """
    C - Convert Celcius to Fahrenheit
    F - Convert Fahrenheit to Celcius
    Q - Quit 
"""
print(MENU)
choice = input("Choose a menu: ")
while choice != "Q":
    if choice == "C":
        celcius = float(input("Celcius: "))
        fahrenheit = celcius * 9.0 / 5 + 32
        print("Result = {:.2f} F ".format(fahrenheit))
    elif choice == "F":
        fahrenheit = float(input("Fahrenheit: "))
        celcius = 5/9 * (fahrenheit - 32)
        print("Result = {:.2f} C".format(celcius))
    else :
        print("Invalid Option")
    print(MENU)
    choice = choice = input("Choose a menu: ")
print("Thank you")