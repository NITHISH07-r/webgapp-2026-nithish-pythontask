import os
def add_employee():
    emp_id=input("enter employee ID: ")
    name=input("enter name: ")
    salary=input("enter salary: ")
    with open("sample.txt","a") as file:
        file.write(f"{emp_id},{name},{salary}\n")
    print("employee added successfully")
def view_employees():
    if not os.path.exists("sample.txt"):
        print("no employee records found")
        return
    with open("sample.txt","r") as file:
        records=file.readlines()
        print(records)
    if not records:
        print("no employee records found")
        return
    print("\nemployee records")
    print("-"*30)
    for record in records:
        emp_id,name,salary=record.strip().split(",")
        print(f"ID:{emp_id}|Name:{name}|Salary:{salary}")
def search_employee():
    emp_id=input("enter employee id to search: ")
    found=False
    if os.path.exists("sample.txt"):
        with open("sample.txt","r") as file:
            for record in file:
                eid,name,salary=record.strip().split(",")
                if eid == emp_id:
                    print("\nEmployee Found")
                    print(f"ID: {eid}")
                    print(f"Name: {name}")
                    print(f"Salary: {salary}")
                    found = True
                    break
    if not found:
        print("employee not found")
def delete_employee():
    emp_id=input("enter employee is to delete: ")
    if not os.path.exists("sample.txt"):
        print("no records found")
        return
    records=[]
    with open("sampe.txt", "r") as file:
        records = file.readlines()
    found = False
    with open("sample.txt", "w") as file:
        for record in records:
            eid, name, salary = record.strip().split(",")
            if eid != emp_id:
                file.write(record)
            else:
                found = True
    if found:
        print("Employee deleted successfully.")
    else:
        print("Employee not found.")
while True:
    print("\n===== Employee Management System =====")
    print("1. Add Employee")
    print("2. View Employees")
    print("3. Search Employee")
    print("4. Delete Employee")
    print("5. Exit")
    choice = input("Enter Choice: ")
    if choice == "1":
        add_employee()
    elif choice == "2":
        view_employees()
    elif choice == "3":
        search_employee()
    elif choice == "4":
        delete_employee()
    elif choice == "5":
        print("Thank You!")
        break
    else:
        print("Invalid Choice")