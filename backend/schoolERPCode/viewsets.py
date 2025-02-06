from rest_framework.generics import (
    ListAPIView,
    RetrieveUpdateDestroyAPIView,
    CreateAPIView,
)
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from django.urls import path


def get_standard_model_viewset(
    queryset,
    serializer,
    basic_serializer,
    permission,
    filter_queryset=lambda self, queryset: queryset,
):

    # Necessary because we can't have access variables of functions inside of class declaration
    class BaseContainer:
        def get_queryset():
            return queryset

        def get_serializer():
            return serializer

        def get_basic_serializer():
            return basic_serializer

        def get_permission():
            return permission

        def get_filter_queryset():
            return filter_queryset

    class AllItems(ListAPIView):
        queryset = BaseContainer.get_queryset()
        permission_classes = [IsAuthenticated]
        serializer_class = BaseContainer.get_basic_serializer()

        def get_queryset(self):
            return BaseContainer.get_filter_queryset()(self, super().get_queryset())

    class AnyItem(RetrieveUpdateDestroyAPIView):
        permission_classes = [IsAuthenticated, DjangoModelPermissions, BaseContainer.get_permission()]
        queryset = BaseContainer.get_queryset()
        serializer_class = BaseContainer.get_basic_serializer()
        lookup_field = "id"

    class CreateItem(CreateAPIView):
        permission_classes = [DjangoModelPermissions, BaseContainer.get_permission()]
        queryset = BaseContainer.get_queryset()
        serializer_class = BaseContainer.get_basic_serializer()
    return [
        path("all", AllItems.as_view()),
        path(
            "<int:id>/",
            AnyItem.as_view(),
        ),
        path(
            "create/",
            CreateItem.as_view(),
        ),
    ]

