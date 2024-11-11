def test_category_init(for_category):
    assert for_category.name == "Мобильные телефоны"
    assert for_category.description == "Iphone"
    assert for_category.products == ["Iphone 14", "Iphone 15 Pro", "Iphone 16 Pro max"]
    assert for_category.category_count == 1
    assert for_category.product_count == 3


def test_category_empty_products(for_category_empty_product):
    assert for_category_empty_product.count_of_products == 3
    assert for_category_empty_product.count_of_categories == 1
