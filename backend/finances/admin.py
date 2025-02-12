from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Purpose, Payee, Record


# Register your models here.
@admin.register(Purpose)
class PurposeAdmin(ImportExportModelAdmin):
    list_display = ["name"]
    search_fields = ["name", "description"]


@admin.register(Payee)
class PayeeAdmin(ImportExportModelAdmin):
    list_display = [
        "name",
        "email",
        "phone",
        "card_id",
        "wallet_id",
        "bank_id",
        "upi_id",
    ]
    search_fields = [
        "name",
        "email",
        "phone",
        "card_id",
        "wallet_id",
        "bank_id",
        "upi_id",
    ]


@admin.register(Record)
class RecordAdmin(ImportExportModelAdmin):
    list_display = [
        "student",
        "amount",
        "datetime",
        "payment_type",
        "payment_id",
        "payment_status",
        "purpose",
        "payee",
    ]
    search_fields = [
        "student",
        "amount",
        "datetime",
        "payment_type",
        "payment_id",
        "payment_status",
        "purpose",
        "payee",
    ]
    list_filter = [
        "student",
        "amount",
        "datetime",
        "payment_type",
        "payment_id",
        "payment_status",
        "purpose",
        "payee",
    ]
