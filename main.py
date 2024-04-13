
from Car import Car
from Car import ElectricCar

if __name__ == 'main':
    my_car = Car(make="Toyota",model="Corolla")
    my_car.start_engine()
    # 100 kWh
    capacity = 100
    unit = "kWh"
    battery_capacity = f"{capacity} {unit}"
    my_electric_car = ElectricCar(make="Tesla",model="Model S",battery_capacity="100 kWh")
    my_electric_car.start_engine()


