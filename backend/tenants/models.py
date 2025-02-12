from django.db import models
from django_tenants.models import TenantMixin, DomainMixin
import razorpay

razorpay_clients = {}

# Create your models here.
class School(TenantMixin):
    name = models.CharField(max_length=100)
    # Ab mujhe dar lagna start ho gaya hai
    razorpay_api_key = models.TextField(null=True)
    razorpay_api_secret = models.TextField(null=True)

    def get_razorpay_client(self):
        if self.id not in razorpay_clients:
            razorpay_clients[self.id] = razorpay.Client(
                auth=(self.razorpay_api_key, self.razorpay_api_secret)
            )
        return razorpay_clients[self.id]



    # default true, schema will be automatically created and synced when it is saved
    auto_create_schema = True

class Domain(DomainMixin):
    pass
