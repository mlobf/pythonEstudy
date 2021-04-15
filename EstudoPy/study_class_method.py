import math
import os


class Pizza:
    def __init__(self, radius, ingredients):
        self.ingredients = ingredients
        self.radius = radius

    def __repr__(self):
        return f"Pizza({self.ingredients})"

    def area(self):
        return self._circle_area(self.radius)

    # _ means that this is a non public and is independent to the rest of
    #     the object. And cant modify the object estate

    @staticmethod  # private static method
    def _circle_area(r):
        return r ** 2 * math.pi

    @classmethod
    def marqueita(cls):
        return cls(["cheese", "tomatoes"])

    @classmethod
    def brasileira(cls):
        return cls(["cheese", "garlic", "catupiry"])


# Pizza(['cheese', 'tomatoes', 'ham', 'tomato', 'onions', 'garlic'])
f = 'farinha'
print(Pizza.marquerita(f))
# print(Pizza.brasileira())

p = Pizza(4.5, ["pinapple", "picles"]).area()
#print(p)


p = Pizza._circle_area(44)
#print(p)



'''
BASE_PATH = (
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    + "/teste_EDI_file/TesteEDI"
)
'''

print(BASE_PATH)
