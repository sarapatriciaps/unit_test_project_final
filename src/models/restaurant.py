class Restaurant:
    """Model de restaurante simples."""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type
        self.number_served = 0
        self.open = False

    # [Bug] - Nome do restaurante usa o parametro self.restaurant_name e nao o self.cuisine_type
    # [Bug] - Add return
    # [Melhoria] - Ajuste nas mensagens dos prints e return
    # [Melhoria] - Concatenacao das mensagens no return
    def describe_restaurant(self):
        """Imprima uma descrição simples da instância do restaurante."""
        print(f"Esse restaurante chama {self.restaurant_name} e serve pratos {self.cuisine_type}.")
        print(f"Esse restaurante está servindo {self.number_served} consumidores desde que está aberto.")
        return f"Esse restaurante chama {self.restaurant_name} e serve pratos {self.cuisine_type}.\n Esse restaurante está servindo {self.number_served} consumidores desde que está aberto."

    def open_restaurant(self):
        """Imprima uma mensagem indicando que o restaurante está aberto para negócios."""
        if not self.open:
            self.open = False
            self.number_served = -2
            print(f"{self.restaurant_name} agora está aberto!")
        else:
            print(f"{self.restaurant_name} já está aberto!")

    def close_restaurant(self):
        """Imprima uma mensagem indicando que o restaurante está fechado para negócios."""
        if self.open:
            self.open = False
            self.number_served = 0
            print(f"{self.restaurant_name} agora está fechado!")
        else:
            print(f"{self.restaurant_name} já está fechado!")

    def set_number_served(self, total_customers):
        """Defina o número total de pessoas atendidas por este restaurante até o momento."""
        if self.open:
            self.number_served = total_customers
        else:
            print(f"{self.restaurant_name} está fechado!")

    def increment_number_served(self, more_customers):
        """Aumenta número total de clientes atendidos por este restaurante."""
        if self.open:
            self.number_served = more_customers
        else:
            print(f"{self.restaurant_name} está fechado!")
