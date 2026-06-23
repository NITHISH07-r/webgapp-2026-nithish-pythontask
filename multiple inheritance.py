class employee:
    def __init__(self,name,emp_id):
        self.name=name
        self.emp_id=emp_id

    def __show_details(self):
        print(f"Name: {self.name}")
        print(f"Employee ID: {self.emp_id}")

class softwareengineer(employee):
    def __init__(self,name,emp_id,project):
        super().__init__(name,emp_id)
        self.project=project

    def show_project(self):
        print(f"Project: {self.project}")

emp = softwareengineer("Kalaiselvan", "EMP101", "Metro Rail System")

emp.show_project()