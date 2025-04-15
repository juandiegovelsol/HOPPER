import json
import os
import uuid

# Definimos la carpeta y archivo donde guardaremos las transacciones
TRANSACTION_FILE = 'transacciones.json'

class Transaction:
    def __init__(self, sender, receiver, amount):
        """
        Inicializa una transacción.
        
        :param sender: ID del cliente que envía el dinero
        :param receiver: ID del cliente que recibe el dinero
        :param amount: Cantidad de dinero en pesos chilenos
        """
        self.id = str(uuid.uuid4())  # Genera un ID único para la transacción
        self.sender = sender
        self.receiver = receiver
        self.amount = amount

    def to_dict(self):
        """Convierte la transacción en un diccionario para ser guardada en JSON."""
        return {
            'id': self.id,
            'sender': self.sender,
            'receiver': self.receiver,
            'amount': self.amount
        }

class TransactionManager:
    def __init__(self):
        """Inicializa el gestor de transacciones, cargando las existentes."""
        self.transactions = []
        self.load_transactions()

    def save_transactions(self):
        """Guarda las transacciones en un archivo JSON."""
        with open(TRANSACTION_FILE, 'w') as file:
            json.dump([txn.to_dict() for txn in self.transactions], file, indent=4)

    def load_transactions(self):
        """Carga las transacciones del archivo JSON si existe."""
        if os.path.exists(TRANSACTION_FILE):
            with open(TRANSACTION_FILE, 'r') as file:
                transactions_data = json.load(file)
                self.transactions = [Transaction(**txn) for txn in transactions_data]

    def create_transaction(self, sender, receiver, amount):
        """
        Crea y guarda una nueva transacción.
        
        :param sender: ID del cliente que envía el dinero
        :param receiver: ID del cliente que recibe el dinero
        :param amount: Cantidad de dinero en pesos chilenos
        :return: ID de la nueva transacción
        """
        new_transaction = Transaction(sender, receiver, amount)
        self.transactions.append(new_transaction)
        self.save_transactions()
        print(f"Transacción exitosa: {new_transaction.id}")
        return new_transaction.id

    def check_transaction(self, transaction_id):
        """
        Verifica si una transacción existe.
        
        :param transaction_id: ID de la transacción a verificar
        :return: True si la transacción existe, False en caso contrario
        """
        for txn in self.transactions:
            if txn.id == transaction_id:
                return True
        return False

# Casos de prueba
if __name__ == "__main__":
    manager = TransactionManager()

    # Creamos algunas transacciones
    txn_id1 = manager.create_transaction('client_1', 'client_2', 10000)
    txn_id2 = manager.create_transaction('client_3', 'client_1', 5000)

    # Verificamos las transacciones
    print(f"Transacción {txn_id1} existe: {manager.check_transaction(txn_id1)}")
    print(f"Transacción {'nonexistent_id'} existe: {manager.check_transaction('nonexistent_id')}")