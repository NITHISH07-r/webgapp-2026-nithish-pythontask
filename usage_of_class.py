class hospital:
    def __init__(self,room,j):
        self.room,self.j=room,j
    
    def display(self):
        for i in range(1,self.room):
            for j in range(self.j,7-i):
               print("*",end=" ")
             
            print(" ")  

s1=hospital(5,2)
s2=hospital(6,1)

s1.display()
s2.display()