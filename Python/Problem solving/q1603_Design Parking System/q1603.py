class ParkingSystem:
    def __init__(self, big, medium, small):
        self.slots = [big, medium, small]
        print(
            f"Initiated car parking system with {big} big, {medium} medium, {small} small slots"
        )

    def addCar(self, carType):
        car_type = carType - 1
        self.slots[car_type] -= 1
        return self.slots[car_type] >= 0


if __name__ == "__main__":
    s = ParkingSystem(1, 1, 0)
    print(s.addCar(1))
    print(s.addCar(2))
    print(s.addCar(3))
    print(s.addCar(1))
