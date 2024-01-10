class Employee:
    def __init__(self):
        self.__dict__["name"] = "John"
        self.__dict__["age"] = 23
        self.__dict__["salary"] = 1000
        self.__dict__["company"] = "Google"
        self.__dict__["position"] = "Software Engineer"
    pass

emp_1 = Employee()
print(emp_1)
print(emp_1.__dict__) # __dict__ is a dictionary that contains all the attributes and values of the object
#Just be notice that in python to construct an object, python use the __new__ method to create the object and then use the __init__ method to initialize the object
