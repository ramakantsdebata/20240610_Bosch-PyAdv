import threading
import time

class BankAccount:
    def __init__(self):
        self.bal= 0
    
    def deposit(self, amt):
        balance = self.bal
        time.sleep(1)       # Simulating a delay
        self.bal= balance + amt
        print(f"Deposit[{amt}]: Balance[{balance} --> {self.bal}]")

    def withdraw(self, amt):
        balance = self.bal
        self.bal= balance - amt
        print(f"Withdraw[{amt}]: Balance[{balance} --> {self.bal}]")

# Employs locking to enfore atomic behaviour on 'self.bal'
class BankAccountWithLock:
    def __init__(self):
        self.bal= 0
        self.lk_bal = threading.Lock()
    
    def deposit(self, amt):
        with self.lk_bal:
            balance = self.bal
            time.sleep(1)       # Simulating a delay
            self.bal= balance + amt
        print(f"Deposit[{amt}]: Balance[{balance} --> {self.bal}]")

    def withdraw(self, amt):
        with self.lk_bal:
            balance = self.bal
            self.bal= balance - amt
        print(f"Withdraw[{amt}]: Balance[{balance} --> {self.bal}]")

def OperateAccount(b):
    t1 = threading.Thread(target=b.deposit, args=(100,))
    t2 = threading.Thread(target=b.withdraw, args=(50,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(f"Final Balance [{b.bal}]")

def Main():
    # Without the Lock
    b1 = BankAccount()
    OperateAccount(b1)
    print()

    # With the Lock in place
    b2 = BankAccountWithLock()
    OperateAccount(b2)

Main()