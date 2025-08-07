class Car:
    def __init__(self):
        self.speed = 0
        self.odometer = 0
        self.time = 0
        print("I'm a car!")

    def accelerate(self):
        self.speed += 5
        self.time += 1
        self.odometer += self.speed  # Line 15: Odometer update

    def brake(self):
        if self.speed >= 5:
            self.speed -= 5
        else:
            self.speed = 0
        self.time += 1
        self.odometer += self.speed

    def get_odometer(self):
        return self.odometer

    def get_average_speed(self):
        if self.time == 0:
            return 0
        return self.odometer / self.time

def main():
    my_car = Car()
    while True:
        action = input("What should I do? [A]ccelerate, [B]rake, show [O]dometer, or show average [S]peed? ").lower()
        if action == 'a':
            my_car.accelerate()
            print("Accelerating...")
        elif action == 'b':
            my_car.brake()
            print("Braking...")
        elif action == 'o':
            print(f"The car has driven {my_car.get_odometer()} kilometers")
        elif action == 's':
            print(f"The car's average speed is {my_car.get_average_speed()} km/h")
        else:
            print("Invalid option, try again.")

if __name__ == "__main__":
    main()