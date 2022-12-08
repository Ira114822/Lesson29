from prod.model.entity import *


class Basket:
    def __init__(self):
        self._products = []

    def add(self, product):
        if isinstance(product, Product):
            self._products.append(product)

    def __len__(self):
        return len(self._products)

    def __bool__(self):
        return len(self._products) != 0


    # def get(self, index):
    #     if isinstance(index, int) and 0 <= index < self.size():
    #         return self._products[index]
    #
    # def size(self):
    #     return len(self._products)

    def __str__(self):
        return f""


basket = Basket()
basket.add(Product())
print(len(basket))