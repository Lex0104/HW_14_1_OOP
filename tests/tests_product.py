def test_product_init(first_product):
    assert first_product.name == "Iphone 15"
    assert first_product.description == "512GB, Gray space"
    assert first_product.price == 210000.0
    assert first_product.quantity == 8


def test_price_init(system, first_product):
    first_product.price = 0.0
    notifications = system.readouterr()
    assert notifications.out.strip() == "Цена не должна быть нулевая или отрицательная"

    first_product.price = -1.0
    notifications = system.readouterr()
    assert notifications.out.strip() == "Цена не должна быть нулевая или отрицательная"

    first_product.price = 15000.0
    assert first_product.price == 15000.0


def test_str_product(first_product):
    assert str(first_product) == "Iphone 15, 210000.0 руб. Остаток: 8 шт."


def test_add_product(first_product, second_product):
    assert first_product + second_product == 1068000.0
