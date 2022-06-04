class Car:
    def __init__(self, color, model, wheels):
        self.color = color
        self.model = model
        self.wheels = wheels

    def car_details (self):
        print("This is a car")

class Ford(Car):
    make = "Ford"

    def __init__(self, color, model, wheels):
        super().__init__(color, model, wheels)

    def car_details (self):
        print(f"This is a {self.color} {self.make} {self.model} with {str(self.wheels)} wheels")


my_car = Ford("blue", "Explorer", 4)
my_car.car_details()
