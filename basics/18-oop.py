class Employee:
    'Common base class for all employees'
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def __del__(self):
        class_name = self.__class__.__name__
        print(class_name, "destroyed")

    def displayCount(self):
        print("Total Employee %d" % Employee.empCount)

    def displayEmployee(self):
        print("Name : ", self.name, ", Salary: ", self.salary)


#"This would create first object of Employee class"
emp1 = Employee("Zara", 2000)
#"This would create second object of Employee class"
emp2 = Employee("Manni", 5000)
emp1.displayEmployee()
emp2.displayEmployee()

print ("Total Employee %d" % Employee.empCount)
print(hasattr(emp1, 'age'))# Returns true if 'age' attribute exists
print(getattr(emp1, 'salary'))# Returns value of 'age' attribute
print(setattr(emp1, 'salary', 8)) # Set attribute 'age' at 8
#print(delattr(emp1, 'salary'))# Delete attribute 'age

print("Employee.__doc__:", Employee.__doc__      )
print("Employee.__name__:", Employee.__name__    )
print("Employee.__module__:", Employee.__module__)
print("Employee.__bases__:", Employee.__bases__  )
print("Employee.__dict__:", Employee.__dict__    )