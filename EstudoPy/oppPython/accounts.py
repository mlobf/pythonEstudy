import datetime
import pytz


class Account:
    """
    Simple class Account with balance.
    """

    @staticmethod
    def _current_time():
        utc_time = datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)

    def __init__(self, name, balance):
        self._name = name
        self._balance = balance
        self._transaction_list = [(Account._current_time(), balance)]
        print("Account created for " + self._name)
        self.show_balance()

#commets


    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print("Balance is {}".format(self._balance))
            self._transaction_list.append((Account._current_time(), amount))

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
        else:
            print(
                "The amount must be gretter then zero and no more then your Account balance"
            )
        self.show_balance()
        self._transaction_list.append((Account._current_time(), -amount))

    def show_balance(self):
        print("Balance is {}".format(self._balance))

    def show_transactions(self):
        for date, amount in self._transaction_list:
            if amount > 0:
                tran_type = "deposited"
            else:
                tran_type = "withdrawn"
                amount *= -1
            print(
                "{:6} {} on  {} (local time was {})".format(
                    amount, tran_type, date, date.astimezone()
                )
            )


if __name__ == "__main__":
    tim = Account("Tim", 0)
    tim.show_balance()

    tim.deposit(1000)
    tim.withdraw(500)
    tim.show_transactions()

    james = Account("James", 800)
    james.deposit(100)
    james.withdraw(200)
    james.show_transactions()
    james.show_balance()
