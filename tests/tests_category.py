def test_category_init(for_category):
    assert for_category.name == "Мобильные телефоны"
    assert for_category.description == "Iphone"
    assert for_category.products == ["Iphone 14", "Iphone 15 Pro", "Iphone 16 Pro max"]
