import datetime

class Vehicle:
    """Base class for all vehicles."""
    
    def __init__(self, colour: str, weight: float, max_speed: float, **kwargs):
        self.colour = colour
        self.weight = weight
        self.max_speed = max_speed
        self.max_range = kwargs.get('max_range', None)
        self.seats = kwargs.get('seats', None)
    
    def move(self, speed: float) -> None:
        print(f"The vehicle is moving at {speed} km/h")


class Car(Vehicle):
    """Represents a car, inheriting from Vehicle."""
    
    def __init__(self, colour: str, weight: float, max_speed: float, form_factor: str, **kwargs):
        super().__init__(colour, weight, max_speed, **kwargs)
        self.form_factor = form_factor
    
    def move(self, speed: float) -> None:
        print(f"The car is driving at {speed} km/h")


class Electric(Car):
    """Electric car subclass."""
    
    def __init__(self, colour: str, weight: float, max_speed: float, form_factor: str, battery_capacity: float, **kwargs):
        super().__init__(colour, weight, max_speed, form_factor, **kwargs)
        self.battery_capacity = battery_capacity
    
    def move(self, speed: float) -> None:
        range_info = f" and has a max range of {self.max_range} km" if self.max_range else ""
        print(f"The electric car is driving at {speed} km/h{range_info}")


class Petrol(Car):
    """Petrol car subclass."""
    
    def __init__(self, colour: str, weight: float, max_speed: float, form_factor: str, fuel_capacity: float, **kwargs):
        super().__init__(colour, weight, max_speed, form_factor, **kwargs)
        self.fuel_capacity = fuel_capacity
    
    def move(self, speed: float) -> None:
        range_info = f" and has a max range of {self.max_range} km" if self.max_range else ""
        print(f"The petrol car is driving at {speed} km/h{range_info}")


class Plane(Vehicle):
    """Represents a plane, inheriting from Vehicle."""
    
    def __init__(self, colour: str, weight: float, max_speed: float, wingspan: float, **kwargs):
        super().__init__(colour, weight, max_speed, **kwargs)
        self.wingspan = wingspan
    
    def move(self, speed: float) -> None:
        print(f"The plane is flying at {speed} km/h")


class Propeller(Plane):
    """Propeller plane subclass."""
    
    def __init__(self, colour: str, weight: float, max_speed: float, wingspan: float, propeller_diameter: float, **kwargs):
        super().__init__(colour, weight, max_speed, wingspan, **kwargs)
        self.propeller_diameter = propeller_diameter
    
    def move(self, speed: float) -> None:
        print(f"The propeller plane is flying at {speed} km/h")


class Jet(Plane):
    """Jet plane subclass."""
    
    def __init__(self, colour: str, weight: float, max_speed: float, wingspan: float, engine_thrust: float, **kwargs):
        super().__init__(colour, weight, max_speed, wingspan, **kwargs)
        self.engine_thrust = engine_thrust
    
    def move(self, speed: float) -> None:
        print(f"The jet is flying at {speed} km/h")


class FlyingCar(Car, Plane):
    """Multiple inheritance example - flying car."""
    
    def __init__(self, colour: str, weight: float, max_speed: float, form_factor: str, wingspan: float, **kwargs):
        super().__init__(colour=colour, weight=weight, max_speed=max_speed, form_factor=form_factor, wingspan=wingspan, **kwargs)
    
    def move(self, speed: float) -> None:
        print(f"The flying car is driving or flying at {speed} km/h")


# Testing the classes
if __name__ == "__main__":
    generic_vehicle = Vehicle("red", 1000, 200)
    generic_vehicle.move(100)

    car = Car("blue", 1500, 250, "SUV")
    car.move(150)

    electric_car = Electric("green", 1200, 200, "Hatchback", 100, max_range=500, seats=5)
    electric_car.move(100)

    petrol_car = Petrol("red", 1500, 250, "SUV", 50, max_range=600)
    petrol_car.move(150)

    plane = Plane("white", 50000, 900, 35)
    plane.move(800)

    flying_car = FlyingCar("red", 1000, 200, "SUV", 30, seats=5)
    flying_car.move(100)
    print(f"Seats: {flying_car.seats}, Wingspan: {flying_car.wingspan}, Form: {flying_car.form_factor}")