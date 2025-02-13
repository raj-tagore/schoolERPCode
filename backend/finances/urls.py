from django.urls import path, include
from .views import purpose_views, payee_views, record_views, create_order, check_order

urlpatterns = [
    path("purpose/", include(purpose_views)),
    path("payee/", include(payee_views)),
    path("record/", include(record_views)),
    path("order/create", create_order),
    path("order/check", check_order),
]
