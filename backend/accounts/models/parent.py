from typing import final

from django.db import models

from accounts.models import Account
from allocation.models.qualification import Qualification


@final
class Parent(models.Model):
    account = models.OneToOneField(
        Account, on_delete=models.CASCADE, related_name="parent"
    )

    occupation = models.CharField("Occupation", max_length=100, blank=False)

    office_address = models.CharField("Office Address", max_length=1000, null=True)

    qualifications = models.ManyToManyField(
        Qualification, related_name="parents", blank=True
    )

    def __str__(self):
        return self.account.username
