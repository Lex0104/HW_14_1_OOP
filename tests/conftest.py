import pytest

from src.category import Category
from src.product import Product
from src.lawn_grass import LawnGrass
from src.smartphone import Smartphone


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


@pytest.fixture
def first_lawn_grass():
    return LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")


@pytest.fixture
def second_lawn_grass():
    return LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15, "США", "5 дней", "Темно-зеленый")


@pytest.fixture
def first_smartphone():
    return Smartphone("Iphone", "512GB", 210000.0, 8, 98.2, "15", 512, "Gray")


@pytest.fixture
def second_smartphone():
    return Smartphone("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14, 90.3, "Note 11", 1024, "Синий")


@pytest.fixture
def category_empty_product():
    return Category(name="Мобильные телефоны", description="Iphone")
