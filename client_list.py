from datetime import datetime
from json import JSONEncoder, dumps


class Client:
    def __init__(self, name, surname, pesel, address, birthday, discount=False):
        self.name = name
        self.surname = surname
        self.pesel = pesel
        self.address = address
        self.birthdate = datetime.strptime(birthday, '%d-%m-%Y')
        self.discount = discount

    def create_client(self):
        data = [('name', self.name), ('surname', self.surname), ('pesel', self.pesel), ('birthdate', self.birthdate),
                ('discount', self.discount)]
        return {(key, value) for (key, value) in data}

    def age(self):
        today = datetime.today()
        age = today.year - self.birthdate.year - ((today.month, today.day) < (self.birthdate.month, self.birthdate.day))
        return age




clients = []
client_1 = Client('Jakub', 'Sokalski', '123456789', 'Romera 10/23, Warszawa', '12-10-1998')
client_2 = Client('Grzegorz', 'Kowalski', '987654321', 'Niepodległości 69, Warszawa', '20-05-1995')
client_3 = Client('Anna', 'Nowak', '213721372', 'Aluzyjna 18/42, Warszawa', '20-03-1996')

clients.append(client_1)
clients.append(client_2)
clients.append(client_3)

for client in clients:
    clients_with_discount = []
    if client.age() in range(18, 27):
        client.discount = True
        clients_with_discount.append(client)
        for discount_client in clients_with_discount:
            discount_client = dumps(discount_client.__dict__, indent=4, sort_keys=True, default=str)

