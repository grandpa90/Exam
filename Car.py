class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def start_engine(self):
        print("Engine started!")


class ElectricCar(Car):
    def __init__(self, make, model,battery_capacity):
        super().__init__(make, model)
        self.battery_capacity = battery_capacity
