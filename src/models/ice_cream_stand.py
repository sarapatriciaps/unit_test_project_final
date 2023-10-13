from src.models.restaurant import Restaurant


class IceCreamStand(Restaurant):
    """Um tipo especializado de restaurante."""

    # [Bug]Inclusao do 'append' para armazenar sabores em lista
    def __init__(self, restaurant_name, cuisine_type, flavors_list):
        """
        Inicialize os atributos da classe pai.
        Em seguida, inicialize os atributos específicos de uma sorveteria.
        """
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors_list

    # [Bug]Add return
    # [Bug]Inclusao do 'append' para armazenar sabores em lista
    # [Melhoria] Mensagem de retorno para 'flavor' invalido
    def flavors_available(self):
        """Percorra a lista de sabores disponíveis e imprima."""
        if self.flavors:
            available_flavors = []
            print("\nNo momento temos os seguintes sabores de sorvete disponíveis:")
            for flavor in self.flavors:
                available_flavors.append(flavor)
                print(f"\t-{flavor}")
            return available_flavors
        else:
            print("Estamos sem estoque atualmente!")
            return []

    # [Bug]Add return
    # [Bug]Correcao para retornar apenas o sabor informado - de: {self.flavors} para: {flavor}
    def find_flavor(self, flavor):
        """Verifica se o sabor informado está disponível."""
        if self.flavors:
            if flavor in self.flavors:
                print(f"Temos no momento {flavor}!")
                return f"Temos no momento {flavor}!"
            else:
                print(f"Não temos no momento {flavor}!")
                return f"Não temos no momento {flavor}!"
        else:
            print("Estamos sem estoque atualmente!")
            return "Estamos sem estoque atualmente!"

    # [Bug] Add return
    # [Melhoria] Add validacao para 'flavor' para aceitar apenas valores do tipo str
    # [Melhoria] Alteracao da mensagem de retorno para 'flavor' invalido
    def add_flavor(self, flavor):
        """Add o sabor informado ao estoque."""
        if flavor is not None and isinstance(flavor, str) and flavor.strip() != "":
            if self.flavors:
                if flavor in self.flavors:
                    print(f"'{flavor}' já disponivel!")
                    return f"'{flavor}' já disponivel!"
                else:
                    self.flavors.append(flavor)
                    print(f"{flavor} adicionado ao estoque!")
                    return f"{flavor} adicionado ao estoque"
        else:
            print("Sabor invalido!")
            return "Sabor invalido!"
