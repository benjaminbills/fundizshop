from oscar.apps.checkout.models import *  # noqa isort:skip

from djmoney.models.fields import MoneyField
from django.db import models
from djmoney.money import Money

class BankAccount(models.Model):
    balance = MoneyField(max_digits=14, decimal_places=2, default_currency='KSH')
    money = MoneyField(max_digits=10, decimal_places=2, null=True, default_currency=None)

account = BankAccount.objects.create()
assert account.money is None
assert account.money_currency is None
