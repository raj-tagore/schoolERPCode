from .models import Purpose, Payee, Record
from .serializers import (
    PurposeSerializer,
    PayeeSerializer,
    BasicPayeeSerializer,
    RecordSerializer,
    BasicRecordSerializer,
)
from schoolERPCode.viewsets import get_standard_model_viewset
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
import json
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


@api_view(["POST"])
@permission_classes([AllowAny])
def create_order(request):
    tenant = getattr(request, "tenant", None)
    if not tenant:
        return Response({"error": "tenant not given"}, status=400)
    if "amount" not in request.data:
        return Response({"error": "amount not given"}, status=400)
    if "purpose" not in request.data:
        return Response({"error": "purpose not given"}, status=400)
    if "student" not in request.data:
        return Response({"error": "student not given"}, status=400)
    client = tenant.get_razorpay_client()
    return Response(
        client.order.create(
            {
                "amount": request.data["amount"],
                "currency": "INR",
                "payment_capture": "1",
                "notes": {
                    "purpose_id": request.data["purpose"],
                    "student_id": request.data["student"],
                    "tenant_id": tenant.id,
                },
            }
        )
    )


# TODO: Implement this properly after adding types everywhere
@api_view(["POST"])
@permission_classes([AllowAny])
def payment_hook(request):
    webhook_body = request.body
    request.data

    return Response(webhook_body)
