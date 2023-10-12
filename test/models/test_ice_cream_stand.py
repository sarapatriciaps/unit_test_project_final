from src.models.ice_cream_stand import IceCreamStand


# checking valid flavor in list - flavors_available()
def test_list_flavor_available():
    ice_cream = IceCreamStand("Frisabor", "Sorvetes", ["Cookies", "Pistache", "Coconut"])
    flavor = "Cookies"

    expected = ice_cream.flavors_available()
    assert expected.__contains__(flavor)


# checking empty list - flavors_available()
def test_list_flavor_in_empty_list_ice_cream_():
    ice_cream = IceCreamStand("Frisabor", "Sorvetes", [])
    expected = ice_cream.flavors_available()
    assert expected == []


def test_find_flavor_available():
    flavors = ["Cookies", "Pistache"]
    ice_cream_stand = IceCreamStand("Frisabor", "Sorvetes", flavors)
    flavor = "Cookies"
    assert ice_cream_stand.find_flavor(flavor) == f"Temos no momento {flavor}!"


def test_find_flavor_not_available():
    flavors = ["Cookies", "Pistache"]
    ice_cream_stand = IceCreamStand("Frisabor", "Sorvetes", flavors)
    flavor = "Coconut"
    assert ice_cream_stand.find_flavor(flavor) == f"Não temos no momento {flavor}!"


# checking add valid flavor - add_flavor()
def test_add_new_flavor():
    flavors = ["Cookies", "Pistache"]
    ice_cream = IceCreamStand("Frisabor", "Sorvetes", flavors)
    flavor = "Coconut"

    expected = f"{flavor} adicionado ao estoque"
    assert ice_cream.add_flavor(flavor) == expected and flavor in ice_cream.flavors


# checking add existent flavor - add_flavor()
def test_add_existent_flavor():
    flavors = ["Cookies", "Pistache"]
    ice_cream = IceCreamStand("Frisabor", "Sorvetes", flavors)
    flavor = "Pistache"

    expected = f"'{flavor}' já disponivel!"
    assert ice_cream.add_flavor(flavor) == expected and flavor in ice_cream.flavors


# checking add empty flavor - add_flavor()
def test_add_invalid_flavor():
    flavors = ["Cookies", "Pistache", "Coconut"]
    ice_cream_stand = IceCreamStand("Frisabor", "Sorvetes", flavors)
    flavor_empty = []
    expected_output = "Sabor invalido!"
    assert ice_cream_stand.add_flavor(flavor_empty) == expected_output
