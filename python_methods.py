class passenger:
    bus_name="red bus"
    def __init__(self,name,fare):
        self.name=name
        self.fare=fare

passengers=[
    passenger("ravi",78),
    passenger("naveen",97),
    passenger("suresh",45),
    passenger("mohit",60)
]

for passenger in passengers:
    print(passenger.name,passenger.fare,passenger.bus_name)