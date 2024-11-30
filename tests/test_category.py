from src.product import Product


def test_category_init(for_category):
    assert for_category.name == "Мобильные телефоны"
    assert for_category.description == "Iphone"
    assert for_category.products == ["Iphone 14", "Iphone 15 Pro", "Iphone 16 Pro max"]
    assert for_category.category_count == 1
    assert for_category.product_count == 3


def test_category_empty_products(for_category_empty_product):
    assert for_category_empty_product.count_of_products == 3
    assert for_category_empty_product.count_of_categories == 1


def test_products_property(for_category):
    assert (
        for_category.products == "Iphone 14, 70000.0 руб. Остаток: 8 шт.\nIphone 15 Pro, 95000.0 руб. Остаток: 7 шт.\n"
    )


def test_str_category(for_category):
    assert str(for_category) == "Мобильные телефоны, количество продуктов: 15 шт."


def test_middle_price(for_category, category_empty_product):
    assert for_category.middle_price() == 81666.667
    assert category_empty_product.middle_price() == 0


def test_my_exception(capsys, for_category):
    assert len(for_category.products_list) == 2

    product_add = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    for_category.add_product(product_add)
    message = capsys.readouterr()
    assert message.out.strip().split("\n")[-2] == "Товар добавлен успешно"
    assert message.out.strip().split("\n")[-1] == "Обработка добавления товара завершена"
