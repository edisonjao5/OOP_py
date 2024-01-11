class Department:
    def __init__(self, name, user, role):
        self.name = name
        self.user = user
        self.role = role

department_1 = Department("IT", "John", "Software Engineer")
print(department_1.__dict__)
department_2 = Department("HR", "Mary", "HR Manager")
print(department_2)