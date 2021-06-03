class Product:

    def __init__(self, value):
        self.__price = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Prize cannot be negative")
        self.__price = value

    @price.deleter
    def price(self):
        del self.__price



