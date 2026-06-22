class passenger:
    def __init__(self,name,fare):
        self.name=name
        self.fare=fare

    def display(self):
        print("name: ",self.name)
        print("fare: ",self.fare)


passengers=[
    passenger("ravi",78),
    passenger("naveen",97),
    passenger("suresh",45),
    passenger("mohit",60)
]

for passenger in passengers:
    passenger.display()

i=0
total_fare=0

while i<len(passengers):
    if passengers[i].fare >=0:
      total_fare += passengers[i].fare

    i +=1 

print("Total fare costed for the passengers to travel: ",total_fare)
