from django.db import models
from accounts.models import Student


class Purpose(models.Model):
    name = models.TextField()
    description = models.TextField()


class Payee(models.Model):
    account_no = models.TextField()
    name = models.TextField()
    email = models.EmailField()
    phone = models.TextField(max_length=15)
    card_id = models.TextField(max_length=32)
    wallet_id = models.TextField(max_length=32)
    bank_id = models.TextField(max_length=32)
    upi_id = models.TextField(max_length=32)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["account_no", "card_id", "wallet_id", "bank_id", "upi_id"],
                name="unique_payee",
            ),
        ]


class Record(models.Model):
    PAYMENT_TYPES = [
        ("UPI", "UPI"),
        ("BAN", "Bank"),
        ("CAS", "Cash"),
        ("CHE", "Cheque"),
    ]
    PAYMENT_STATUSES = [("S", "Sucess"), ("P", "Pending"), ("F", "Failed")]
    student = models.ForeignKey(Student, null=False, on_delete=models.CASCADE)
    amount = models.IntegerField(null=False)
    datetime = models.DateTimeField(auto_now_add=True)
    payment_type = models.CharField(null=True, choices=PAYMENT_TYPES)
    payment_id = models.IntegerField(null=True)
    payment_status = models.CharField(choices=PAYMENT_STATUSES, null=True)
    purpose = models.ForeignKey(Purpose, null=False, on_delete=models.CASCADE)
    payee = models.ForeignKey(Payee, null=True, on_delete=models.CASCADE)
