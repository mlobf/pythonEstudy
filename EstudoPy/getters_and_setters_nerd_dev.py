# Getters and Setters
"""
  The main reason to use getter and setters is
  ensure the data encapsulation so no external 
  access can exploit that data.

  In Python, we define getters and setters to avoid direct
  access or external manipulation
"""


class Developer:
    def __init__(self, name, age, salary, company_name):
        self.name = name
        self.age = age
        self.company_name = company_name

    @property
    def company(self):
        return self.company_name

    @company.setter
    def company(self, company_name):
        self.company_name = company_name


dev_object = Developer("Marcos", 39, 70000, "Google")

dev_object.company_name = "Mappin"

print(dev_object.company_name)