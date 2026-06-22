class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    def display(self):
        print("name: ",self.name)
        print("mark: ",self.marks)
        
        if self.marks >= 50:
            print("result: pass")
        else:
            print("result: fail")

students=[
    student("ravi",78),
    student("naveen",97),
    student("suresh",45),
    student("mohit",60)
]

for student in students:
    student.display()

i=0
pass_count=0
fail_count=0

while i<len(students):
    if students[i].marks >= 50:
      pass_count+=1
    else:
      fail_count+=1

    i +=1 

print("number of students passed: ",pass_count)
print("number of students failed: ",fail_count)

