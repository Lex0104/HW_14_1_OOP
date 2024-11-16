import pytest

from src.category import Category
from src.product import Product


@pytest.fixture
def first_product():
    return Product("Iphone 15", "512GB, Gray space", 210000.0, 8)


@pytest.fixture
def second_product():
    return Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет", 180000.0, 5)


@pytest.fixture
def for_category():
    return Category(
        name="Мобильные телефоны",
        description="Iphone",
        products=["Iphone 14", "Iphone 15 Pro", "Iphone 16 Pro max"],
    )


@pytest.fixture
def empty_product():
    return Category(name="Мобильные телефоны", description="Iphone")
