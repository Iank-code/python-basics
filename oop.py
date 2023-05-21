class Car:

    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    def drive(self):
        print("This car is driving")

    def stop(self):
        print(("This car just stopped"))


car_1 = Car("Toyota", "Mark X", 2020, "Silver")
print(car_1.make)
print(car_1.make)
print(car_1.year)
print(car_1.color)

car_1.drive()
car_1.stop()
