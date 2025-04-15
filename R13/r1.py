# Asegúrate de instalar tinydb antes de ejecutar este script:
# pip install tinydb

from tinydb import TinyDB, Query
import uuid

# Clase que representa una transacción individual
class Transaction:
    def __init__(self, sender_id, receiver_id, amount):
        self.transaction_id = str(uuid.uuid4())  # Generar un ID único para identificar la transacción
        self.sender_id = sender_id
        self.receiver_id = receiver_id
        self.amount = amount

# Clase que maneja las transacciones
class TransactionManager:
    def __init__(self):
        self.db = TinyDB('transactions.json')  # Base de datos para almacenar transacciones en un archivo JSON

    def create_transaction(self, sender_id, receiver_id, amount):
        # Crear y registrar una nueva transacción
        transaction = Transaction(sender_id, receiver_id, amount)
        self.db.insert({'transaction_id': transaction.transaction_id,
                        'sender_id': transaction.sender_id,
                        'receiver_id': transaction.receiver_id,
                        'amount': transaction.amount})
        print(f"Transacción {transaction.transaction_id} creada exitosamente. {amount} pesos chilenos enviados de {sender_id} a {receiver_id}.")

    def check_transaction(self, transaction_id):
        # Comprobar si una transacción específica existe en la base de datos
        TransactionQuery = Query()
        result = self.db.search(TransactionQuery.transaction_id == transaction_id)
        if result:
            print(f"La transacción con ID {transaction_id} es válida y se encuentra en la base de datos.")
            return True
        else:
            print(f"No se ha encontrado ninguna transacción con ID {transaction_id}.")
            return False

# Casos de prueba
def run_tests():
    tm = TransactionManager()

    # Crear transacciones de prueba
    tm.create_transaction('cliente1', 'cliente2', 10000)  # Simular una transacción de 10,000 pesos
    tm.create_transaction('cliente2', 'cliente3', 5000)   # Simular una transacción de 5,000 pesos

    # Obtén una ID de transacción válida para pruebas
    valid_transaction_id = tm.db.all()[0]['transaction_id']

    # Probar una transacción válida
    tm.check_transaction(valid_transaction_id)
    
    # Probar una transacción inválida
    tm.check_transaction('invalid_transaction_id')

# Ejecutar casos de prueba
if __name__ == "__main__":
    run_tests()