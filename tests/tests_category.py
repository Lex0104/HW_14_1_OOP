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
        for_category.products == "Iphone 14, 70000.0 руб. Остаток: 2 шт.\nIphone 15 Pro, 95000.0 руб. Остаток: 3 шт.\n"
    )


def test_str_category(for_category):
    assert str(for_category) == "Мобильные телефоны, количество продуктов: 15 шт."
