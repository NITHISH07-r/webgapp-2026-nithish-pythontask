class passenger:
    bus_name = "red bus"

    def __init__(self, name, fare):
        self.name = name
        self.fare = fare

    @classmethod
    def change_bus_name(cls, new_name):
        cls.bus_name = new_name

passengers = [
    passenger("ravi", 78),
    passenger("naveen", 97),
    passenger("suresh", 45),
    passenger("mohit", 60)
]

passenger.change_bus_name("blue bus")

for passenger in passengers:
    print(passenger.name, passenger.fare, passenger.bus_name)
