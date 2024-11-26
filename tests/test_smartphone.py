import pytest


def test_smartphone_init(first_smartphone):
    assert first_smartphone.name == "Iphone 15"
    assert first_smartphone.description == "512GB"
    assert first_smartphone.price == 210000.0
    assert first_smartphone.quantity == 8
    assert first_smartphone.efficiency == 98.2
    assert first_smartphone.model == "15"
    assert first_smartphone.memory == 512
    assert first_smartphone.color == "Gray space"


def test_smartphone_add(first_smartphone, second_smartphone):
    assert first_smartphone + second_smartphone == 2114000.0


def test_smartphone_add_raise(first_smartphone, first_lawn_grass):
    with pytest.raises(TypeError):
        return first_smartphone + first_lawn_grass
