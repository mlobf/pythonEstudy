# Getters and Setters - By Otavio Miranda

# Conceito de Getter
# Obtem um valor

# Conceito de Setter
# Configura um valor


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def discount(self, percent):
        self.price = self.price - (self.price * (percent / 100))
        return print(self.price)

    # Getter - name
    @property
    def name(self):
        return self._name

    # Setter - name -> E tipo um filtro, uma proteção para so meus atributos
    @name.setter
    def name(self, valor):
        self._name = valor.title()

    # Getter - price
    @property
    def price(self):
        return self._price

    # Setter - price
    @price.setter
    def price(self, valor):
        if isinstance(valor, str):
            valor = float(valor.replace("R$", ""))
        self._price = valor


p1 = Product("SHIRT", 50)
p1.discount(10)
print(p1.name, p1.price)


p2 = Product("CUP", "R$15")
p2.discount(10)
print(p2.name, p2.price)
