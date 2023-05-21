# Error handling
try:
    numerator = int(input("Input first number: "))
    denominator = int(input("Input second number: "))
    result = numerator / denominator
except ValueError as e:
    print(e)
    print("Enter only numbers")
except ZeroDivisionError as e:
    print(e)
    print("Can't be divided by 0")
else:
    print(result)