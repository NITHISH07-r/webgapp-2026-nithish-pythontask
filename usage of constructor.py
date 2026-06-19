class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print(self.name,self.age)

s1=student("shaai",101)
s2=student("jenish",103)
s3=student("sherwin",104)

s1.display()
s2.display()
s3.display()

