def annual_salary(monthly_salary):
    return monthly_salary * 12
salary=float(input("enter your montly salary: "))
annual=annual_salary(salary)
print("annual salary: ",annual)