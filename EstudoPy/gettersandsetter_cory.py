"""
  The Property Decorator
    Allows us to define a method and access as 
    atributte
"""


class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def fullname(self):
        return "{} {}".format(self.first, self.last)

    @property
    def email(self):
        return "{} {}@email.com".format(self.first, self.last)


emp_1 = Employee("John", "Smith")


emp_1.first = "Mario"

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)
