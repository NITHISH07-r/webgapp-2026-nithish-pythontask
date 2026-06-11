def create_employee(name, *skills, **details):
    print("Name:", name)

    print("Skills:")
    for skill in skills:
        print("-", skill)

    print("Details:")
    for key, value in details.items():
        print(key, ":", value)

create_employee(
    "ravi",
    "Python",
    "react",
    "MySQL",
    age=25,
    salary=25000,
    city="madurai"
)

