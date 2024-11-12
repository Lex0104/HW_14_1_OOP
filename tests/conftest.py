import pytest

from src.category import Category
from src.product import Product


@pytest.fixture
def first_product():
    return Product("Iphone 15", "512GB, Gray space", 210000.0, 8)


@pytest.fixture
def for_category():
    return Category(
        name="Мобильные телефоны",
        description="Iphone",
        products=[Product("Iphone 1", "Iphone 14", 70000.0, 2), Product("Iphone 2", "Iphone 15 Pro", 95000.0, 3)],
    )


@pytest.fixture
def empty_product():
    return Category(name="Мобильные телефоны", description="Iphone")
