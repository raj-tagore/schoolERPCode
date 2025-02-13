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
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from types import SimpleNamespace
from tenants.models import School
from django_tenants.utils import tenant_context
import json
from django.db.models import Sum
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
    if "order_id" in kwargs:
        queryset = queryset.filter(order_id=kwargs["order_id"])
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
@permission_classes([IsAuthenticated])
def create_order(request):
    tenant = getattr(request, "tenant", None)
    # The default amount is the amount pending
    student = getattr(request.user, "student_account", None)
    if not tenant:
        return Response({"error": "tenant not given"}, status=400)
    if "amount" in request.data:
        amount = request.data["amount"]
    if "purpose" in request.data:
        purpose = request.data["purpose"]
    if "student" in request.data:
        student = request.data["student"]
    amount = Record.objects.filter(student=student).aggregate(Sum("amount"))[
        "amount__sum"
    ]

    if amount and amount < 0:
        amount = -amount

    purpose = getattr(
        Record.objects.filter(student=student).filter(amount__lt=0).last(),
        "purpose",
        None,
    )

    client = tenant.get_razorpay_client()
    order = client.order.create(
        {
            "amount": amount,
            "currency": "INR",
            "notes": {
                "purpose_id": purpose,
                "student_id": student,
                "tenant_id": tenant.id,
            },
        }
    )

    Record.objects.create(
        student_id=student,
        amount=amount,
        order_id=order.id,
        purpose_id=purpose,
        payment_status="P",
    )

    return Response(order)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def verify_payment(request):
    tenant = getattr(request, "tenant", None)
    if not tenant:
        return Response({"error": "tenant not given"}, status=400)
    client = tenant.get_razorpay_client()
    client.utility.verify_payment_signature(
        {
            "razorpay_order_id": request.data["razorpay_order_id"],
            "razorpay_payment_id": request.data["razorpay_payment_id"],
            "razorpay_signature": request.data["razorpay_signature"],
        }
    )
    order = client.order.fetch(request.data["order_id"])
    last_record = Record.objects.filter(order_id=order.id).last()
    if last_record:
        if last_record.payment_status == "S":
            return Response({"error": "Payment already successful"}, status=400)
        else:
            if order["status"] == "paid":
                last_record.payment_status = "S"
                last_record.save()
                client.payment.capture(
                    request.data["razorpay_payment_id"],
                    {"amount": order["amount"], "currency": "INR"},
                )
        return Response(last_record)
    else:
        return Response({"error": "Order not found"}, status=400)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def check_order(request):
    tenant = getattr(request, "tenant", None)
    if not tenant:
        return Response({"error": "tenant not given"}, status=400)
    client = tenant.get_razorpay_client()
    order = client.order.fetch(request.data["order_id"])
    last_record = Record.objects.filter(order_id=order.id).last()
    if last_record:
        if last_record.payment_status == "S":
            return Response({"error": "Payment already successful"}, status=400)
        else:
            if order["status"] == "paid":
                last_record.payment_status = "S"
                last_record.save()
        return Response(last_record)
    else:
        return Response({"error": "Order not found"}, status=400)
