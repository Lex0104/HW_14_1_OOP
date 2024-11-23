class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, new_dict_product, products=None):
        if products:
            for product in products:
                if product.name == new_dict_product["name"]:
                    product.quantity += new_dict_product["quantity"]
                    product.price = max([product.price, new_dict_product["price"]])
                    return product
        return cls(
            new_dict_product["name"],
            new_dict_product["description"],
            new_dict_product["price"],
            new_dict_product["quantity"],
        )

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price: float):
        if price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return
        if price < self.__price:
            check = input("Изменять цену? Введите y если да,и n если нет.\n")
            if check != "y":
                return
        self.__price = price

    def __str__(self):
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if type(other) is self.__class__:
            return self.__price * self.quantity + other.price * other.quantity
        raise TypeError
