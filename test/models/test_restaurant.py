import pytest
from src.models.restaurant import Restaurant


# checking describe restaurant - describe_restaurant()
def test_describe_restaurant():
    restaurant = Restaurant("Cozinha Brasileira", "Comida tipica")

    expected = f"Esse restaurante chama {restaurant.restaurant_name} e serve pratos {restaurant.cuisine_type}.\n Esse restaurante está servindo {restaurant.number_served} consumidores desde que está aberto."
    result = restaurant.describe_restaurant()
    assert result == expected


# checking open restaurant - open_restaurant()
def test_open_restaurant():
    restaurant = Restaurant("Cozinha Brasileira", "Comida tipica", )
    expected = f"{restaurant.restaurant_name} agora está aberto!"
    result = restaurant.open_restaurant()
    assert result == expected


# checking the opening of an already open restaurant - open_restaurant()
def test_open_restaurant_already_open():
    restaurant = Restaurant("Cozinha Brasileira", "Comida tipica")
    expected = f"{restaurant.restaurant_name} já está aberto!"
    restaurant.open_restaurant()

    result = restaurant.open_restaurant()
    assert result == expected


# checking open a closed restaurant - open_restaurant() and close_restaurant()
def test_open_restaurant_when_closed():
    restaurant = Restaurant("Cozinha Brasileira", "Comida tipica")
    restaurant.close_restaurant()

    expected = f"{restaurant.restaurant_name} agora está aberto!"
    result = restaurant.open_restaurant()
    assert result == expected


# checking close a closed restaurant - close_restaurant()
def test_close_restaurant_when_closed():
    restaurant = Restaurant("Cozinha Brasileira", "Comida tipica")

    expected = f"{restaurant.restaurant_name} já está fechado!"
    result = restaurant.close_restaurant()
    assert result == expected


# checking set_number_served when closed restaurant - close_restaurant and set_number_served()
def test_set_number_served_when_closed():
    restaurant = Restaurant("Cozinha Brasileira", "Comida tipica")
    restaurant.close_restaurant()

    result = restaurant.set_number_served(50)
    expected = f"{restaurant.restaurant_name} está fechado!"
    assert result == expected


# checking set_number_served when opened restaurant - open_restaurant() and set_number_served()
def test_set_number_served_when_opened():
    restaurant = Restaurant("Cozinha Brasileira", "Comida tipica")
    expected = restaurant.open_restaurant()

    number_served = 50
    result = restaurant.set_number_served(number_served)
    assert expected == f"{restaurant.restaurant_name} agora está aberto!"
    assert result == number_served


# checking increment_number_served when closed restaurant - close_restaurant() and close_restaurant()
def test_increment_number_served_when_closed():
    restaurant = Restaurant("Cozinha Brasileira", "Comida tipica")
    restaurant.close_restaurant()

    result = restaurant.increment_number_served(10)
    assert f"{restaurant.restaurant_name} está fechado!" in result


# checking increment_number_served when closed restaurant - close_restaurant() and close_restaurant()
def test_increment_number_served_when_opened():
    restaurant = Restaurant("Cozinha Brasileira", "Comida tipica")
    restaurant.open_restaurant()

    result = restaurant.increment_number_served(10)
    assert f"{restaurant.number_served} clientes incrementados." == result
