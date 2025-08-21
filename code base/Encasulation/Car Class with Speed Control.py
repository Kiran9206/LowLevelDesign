'''2. Car Class with Speed Control
Task: Design a Car class with:
Private attributes: speed and fuel_level.
Public methods: accelerate(), brake(), and refuel().
Ensure that the speed cannot be set directly (use methods to increase or decrease speed).
Fuel level should only be modified through the refuel() method.'''



class Car:

    def __init__(self, speed=0, fuel_level=0, max_fuel=100):
        # Ensure default values are set correctly
        self.__speed = speed
        self.__fuel_level = fuel_level
        self.__max_fuel = max_fuel  # Max fuel capacity

    # Accelerate Method
    def accelerate(self, increase_by=10):
        self.__speed += increase_by
        print(f"Car is accelerating... Current speed is {self.__speed} kph.")

    # Brake Method
    def brake(self):
        self.__speed = 0  # When car stops, speed goes to 0
        print("Car has stopped!")

    # Refuel Method with limit check
    def refuel(self, amount):
        if self.__fuel_level + amount > self.__max_fuel:
            print(f"Cannot refuel! Max fuel capacity is {self.__max_fuel} liters.")
        else:
            self.__fuel_level += amount
            print(f"Refueled {amount} liters. Current fuel level: {self.__fuel_level} liters.")

    # Getters for speed and fuel level
    def get_speed(self):
        return self.__speed

    def get_fuel_level(self):
        return self.__fuel_level

    # Decrease speed Method
    def decrease_speed(self, decrease_by=10):
        if self.__speed - decrease_by < 0:
            self.__speed = 0  # Can't go below 0 speed
        else:
            self.__speed -= decrease_by
        print(f"Speed is decreasing... Current speed: {self.__speed} kph.")

    

car = Car(speed=20)
car.refuel(500)
car.get_speed()
car.get_fuel_level()
car.accelerate()
car.decrease_speed()
car.brake()




