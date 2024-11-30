from src.product import Product
from src.smartphone import Smartphone


def test_repr_mixin(capsys):
    Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    notice = capsys.readouterr()
    assert notice.out.strip() == "Product(Iphone 15, 512GB, Gray space, 210000.0, 8)"

    Smartphone("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
    notice = capsys.readouterr()
    assert notice.out.strip() == "Smartphone(Xiaomi Redmi Note 11, 1024GB, 31000.0, 14)"
