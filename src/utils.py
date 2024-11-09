import json
import os

from src.category import Category
from src.product import Product


def json_file(path: str) -> dict:
    full_path = os.path.abspath(path)
    with open(full_path, "r", encoding="UTF-8") as file:
        data = json.load(file)
    return data


def json_objects(data):
    category = []
    for product in data:
        products = []
        for product_list in product["products"]:
            products.append(Product(**product_list))
        product["products"] = products
        category.append(Category(**product))
    return category