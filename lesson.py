class Bank:
    def init(self, clients):
        self.clients = clients
        
    def add_user(self,user):
        self.clients.append(user)
        
    def deposit(self, amount, id):
        for client in self.clients:
            if client.id == id:
                client.balance += amount
                
                
    def all_info(self):
        for client in self.clients:
            print('User name:',client.name)
            print('User id:', client.name)
            print('User balance:', client.name)

class Client:
    def init(self, client_id, name, pin, balance=0.0):
        self.client_id = client_id
        self.name = name         
        self.__pin = pin          
        self.balance = balance
        
        self.max_withdrawal_limit = 150000.0 

    def update_name(self, new_name):
        self.name = new_name
        print(f"Имя успешно изменено на: {self.name}")

    def verify_pin(self, input_pin):
        return self.__pin == input_pin
    
    
KaspiBank=Bank([])

Rayana=Client(1111,3000000,'Rayana')
Aldiyar=Client(1112,200000,'Aldiyar')

KaspiBank.all_info()