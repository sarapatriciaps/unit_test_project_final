import pytest
from src.models.restaurant import Restaurant


def test_describe_restaurant():
    restaurant = Restaurant("Cozinha Brasileira", "Comida tipica brasileira")

    # Teste de sucesso
    expected_output = f"Esse restaurante chama {restaurant.restaurant_name} e serve pratos {restaurant.cuisine_type}.\n Esse restaurante está servindo {restaurant.number_served} consumidores desde que está aberto."
    result = restaurant.describe_restaurant()
    assert result == expected_output


# Teste para open_restaurant
def test_open_restaurant():
    restaurant = Restaurant("Meu Restaurante", "Comida Variada")

    # Teste de sucesso
    expected_output = "Meu Restaurante agora está aberto!"
    result = restaurant.open_restaurant()
    assert result == expected_output


# Teste para close_restaurant
def test_close_restaurant():
    restaurant = Restaurant("Meu Restaurante", "Comida Variada")

    # Teste de sucesso
    expected_output = "Meu Restaurante agora está fechado!"
    result = restaurant.close_restaurant()
    assert result == expected_output
