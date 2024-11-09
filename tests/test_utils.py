from unittest.mock import mock_open, patch

from src.utils import json_file, json_objects


@patch("builtins.open", new_callable=mock_open, read_data='[{"name": "Смартфоны", "description": "Iphone"}]')
def test_json_file(mock_file):
    data = json_file("data/products.json")
    assert data == [{"name": "Смартфоны", "description": "Iphone"}]


def test_json_objects():
    result = json_objects(
        [
            {
                "name": "Смартфоны",
                "description": "Смартфоны, как средство не только коммуникации",
                "products": [
                    {
                        "name": "Iphone 15",
                        "description": "512GB, Gray space",
                        "price": 210000.0,
                        "quantity": 8,
                    }
                ],
            }
        ]
    )
    assert result[0].name == "Смартфоны"