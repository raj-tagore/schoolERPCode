from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from django.urls import path


def get_standard_model_viewset(model, serializer, basic_serializer, permission, filter_queryset=lambda x: x):
    class BaseStandardApiViewset:
        @classmethod
        def get_urls(cls):
            return [
                path("", cls.AllItems.as_view(), name=f"{cls.__name__.lower()}-list"),
                path("<int:id>/", cls.AnyItem.as_view(), name=f"{cls.__name__.lower()}-detail"),
                path("create/", cls.CreateItem.as_view(), name=f"{cls.__name__.lower()}-create"),
            ]

        class AllItems(ListAPIView):
            queryset = model.queryset
            permission_classes = .permission_classes
            queryset = BaseStandardApiViewset.queryset
            serializer_class = BaseStandardApiViewset.serializer_class

        class AnyItem(RetrieveUpdateDestroyAPIView):
            permission_classes = [IsAuthenticated, DjangoModelPermissions]
            queryset = BaseStandardApiViewset.queryset
            serializer_class = BaseStandardApiViewset.serializer_class
            lookup_field = "id"

        class CreateItem(CreateAPIView):
            permission_classes = [DjangoModelPermissions]
            queryset = BaseStandardApiViewset.queryset
            serializer_class = BaseStandardApiViewset.serializer_class
        
