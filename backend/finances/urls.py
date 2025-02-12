from django.urls import path, include
from .views import purpose_views, payee_views, record_views

urlpatterns = [
    path("purpose/", include(purpose_views)),
    path("payee/", include(payee_views)),
    path("record/", include(record_views)),
]
