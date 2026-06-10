
employee={}
emp_count=int(input("enter the number of employees: "))
for i in range(1,emp_count+1):
    name=input("enter the name of the employee: ")
    salary=int(input("enter salary of the employee: "))
    employee[name]=salary
print(employee)
highest_salary = max(employee.values())
print(highest_salary)



