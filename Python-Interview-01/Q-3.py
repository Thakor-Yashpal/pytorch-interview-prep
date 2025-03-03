class employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

e1 = employee("John", 22, 20000)  # Correct way to create an employee object
print(e1.name, e1.age)   
