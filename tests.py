import pytest

from credit_account import CreditAccount


def test_comparation():
    credit_account_1 = CreditAccount("Lukas Novak")
    credit_account_2 = CreditAccount("Pepa Novak", initial_credits=200)

    assert credit_account_1 < credit_account_2
    assert credit_account_2 > credit_account_1
    assert credit_account_1 <= credit_account_2
    assert credit_account_2 >= credit_account_1
    assert credit_account_1 != credit_account_2
    assert not (credit_account_1 == credit_account_2)

    with pytest.raises(TypeError):
        credit_account_1 < 10

    with pytest.raises(TypeError):
        credit_account_1 > 10

    with pytest.raises(TypeError):
        credit_account_1 <= 10

    with pytest.raises(TypeError):
        credit_account_1 >= 10


def test_comparation_eq():
    credit_account_1 = CreditAccount("Lukas Novak", initial_credits=200)
    credit_account_2 = CreditAccount("Pepa Novak", initial_credits=200)

    assert credit_account_1 <= credit_account_2
    assert credit_account_2 >= credit_account_1
    assert not (credit_account_1 != credit_account_2)
    assert credit_account_1 == credit_account_2


def test_balance_operations():
    credit_account_1 = CreditAccount("Lukas Novak", initial_credits=50)
    credit_account_2 = CreditAccount("Pepa Novak", initial_credits=200)

    assert credit_account_1 + credit_account_2 == 250
    assert credit_account_1 - credit_account_2 == -150


def test_docstrings():
    assert CreditAccount.__doc__ is not None
    assert CreditAccount.from_csv.__doc__ is not None
    assert CreditAccount.credit_to_money.__doc__ is not None
    assert CreditAccount.balance.__doc__ is not None
    assert CreditAccount.transfer_to.__doc__ is not None
