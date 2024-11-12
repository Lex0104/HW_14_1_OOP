from src.product import Product


class Category:
    name: str
    description: str
    products: list
    category_count = 0
    product_count = 0

    def __init__(self, name: object, description: object, products: object = None) -> object:
        self.name = name
        self.description = description
        self.__products = products if products else []
        Category.category_count += len(products) if products else 0
        Category.product_count += 1

    def add_product(self, product: Product):
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self):
        products_str = ""
        for product in self.__products:
            products_str += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
            return products_str

    @property
    def products_list(self):
        return self.__products
