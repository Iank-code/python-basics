import time
# While loop

# name = ""
# while len(name) == 0:
#     name = input("Enter your name: ")
#
# print("Hello " + name)


# For loop
# for i in range(10):
#     print(i+1)

# for i in range(50, 100, 2):
#     print(i)

# for i in "Bro Code":
#     print(i)

# for seconds in range(10, 0, -1):
#     print(seconds)
#     time.sleep(1)
#
# print("Happy new year")

# Nested Loop
# rows = int(input("How many rows?: "))
# columns = int(input("How many columns?: "))
# symbol = input("Enter a symbol to use: ")
#
# for i in range(rows):
#     for i in range(columns):
#         print(symbol, end="")
#     print()

# *args

# def add(*args):
#     sum = 0
#     for i in args:
#         sum += i
#     return sum
#
# print(add(1, 2, 3,12,34,1))

# **kwargs
def hello(**kwargs):
    # print("Hello " + kwargs["first"] + " " + kwargs["last"])
    for key,value in kwargs.items():
        print(key + ": " + value)

hello(first="Bro", middle="Dude", last="Code")