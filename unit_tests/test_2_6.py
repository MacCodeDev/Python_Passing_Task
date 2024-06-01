import pytest
from task_2_6 import BankAccount

def test_bank_account():
    account = BankAccount()

    account.deposit(100)
    assert account.get_balance() == 100

    account.withdraw(50)
    assert account.get_balance() == 50

    with pytest.raises(ValueError):
        account.deposit(-100)

    with pytest.raises(ValueError):
        account.withdraw(-50)

    with pytest.raises(ValueError):
        account.withdraw(100)