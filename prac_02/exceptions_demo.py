try:
    numerator = int(input("Enter a numerator: "))
    denominator = int(input("Enter a denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be a valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero")
print("Finished")