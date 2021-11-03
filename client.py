class Client:
    def __init__(self, name_lastname, cash):
        self.name_lastname = name_lastname
        self.cash = cash

    def get_client(self):
        return self.name_lastname
    def get_balance(self):
        return self.cash

newClient = Client("Иван Петров",50)
print("Клиент:" + newClient.get_client())
print("Баланс: " + str(newClient.get_balance()))