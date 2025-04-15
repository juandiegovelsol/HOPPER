CREDIT_PRICE = 1000
def __init__(self, student):

    self.student = student
    self.balance = 0
    self.loans = {}

def __str__(self):

    return f"Name: {self.student.name}\nID: {self.student.id}\nBalance: ${self.balance}"

__repr__ = __str__


def makePayment(self, amount):

    self.balance -= amount
    return self.balance

def chargeAccount(self, amount):

    self.balance += amount
    return self.balance