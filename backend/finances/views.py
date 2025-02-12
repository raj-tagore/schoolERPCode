from .models import Purpose, Payee, Record
from .serializers import (
    PurposeSerializer,
    PayeeSerializer,
    BasicPayeeSerializer,
    RecordSerializer,
    BasicRecordSerializer,
)
from schoolERPCode.viewsets import get_standard_model_viewset
# Create your views here.


def purpose_filter(self, queryset, **kwargs):
    if "name" in kwargs:
        queryset = queryset.filter(name__icontains=kwargs["name"])
    if "description" in kwargs:
        queryset = queryset.filter(description__icontains=kwargs["description"])


purpose_views = get_standard_model_viewset(
    queryset=Purpose.objects.all(),
    serializer_class=PurposeSerializer,
    basic_serializer_class=PurposeSerializer,
    filter_queryset=purpose_filter,
)


def payee_filter(self, queryset, **kwargs):
    if "name" in kwargs:
        queryset = queryset.filter(name__icontains=kwargs["name"])
    if "email" in kwargs:
        queryset = queryset.filter(email__icontains=kwargs["email"])
    if "phone" in kwargs:
        queryset = queryset.filter(phone__icontains=kwargs["phone"])


payee_views = get_standard_model_viewset(
    queryset=Payee.objects.all(),
    serializer_class=PayeeSerializer,
    basic_serializer_class=BasicPayeeSerializer,
    filter_queryset=payee_filter,
)


def record_filter(self, queryset, **kwargs):
    if "student" in kwargs:
        queryset = queryset.filter(student=kwargs["student"])
    if "amount_start" in kwargs:
        queryset = queryset.filter(amount__gte=kwargs["amount_start"])
    if "amount_end" in kwargs:
        queryset = queryset.filter(amount__lte=kwargs["amount_end"])
    if "datetime_start" in kwargs:
        queryset = queryset.filter(datetime__gte=kwargs["datetime_start"])
    if "datetime_end" in kwargs:
        queryset = queryset.filter(datetime__lte=kwargs["datetime_end"])
    if "payment_type" in kwargs:
        queryset = queryset.filter(payment_type=kwargs["payment_type"])
    if "payment_id" in kwargs:
        queryset = queryset.filter(payment_id=kwargs["payment_id"])
    if "payment_status" in kwargs:
        queryset = queryset.filter(payment_status=kwargs["payment_status"])
    if "purpose" in kwargs:
        queryset = queryset.filter(purpose=kwargs["purpose"])
    if "payee" in kwargs:
        queryset = queryset.filter(payee=kwargs["payee"])


record_views = get_standard_model_viewset(
    queryset=Record.objects.all(),
    serializer_class=RecordSerializer,
    basic_serializer_class=BasicRecordSerializer,
    filter_queryset=record_filter,
)
