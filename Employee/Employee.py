class Employee:
    def __init__(self):
        self.__dict__["name"] = "John"
        self.__dict__["age"] = 23
        self.__dict__["salary"] = 1000
        self.__dict__["company"] = "Google"
        self.__dict__["position"] = "Software Engineer"
        self.email = "coded5@dev.com"

        def increase_salary(employee, percent):
            employee.salary += employee.salary * (percent/100)

        def __str__(self):
            return f"Employee {self.name} is {self.age} years old and works as {self.position} in {self.company}"


emp_1 = Employee()
print(emp_1)
print(emp_1.__dict__) # __dict__ is a dictionary that contains all the attributes and values of the object
#Just be notice that in python to construct an object, python use the __new__ method to create the object and then use the __init__ method to initialize the object
