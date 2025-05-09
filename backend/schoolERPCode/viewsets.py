from rest_framework.generics import (
    ListAPIView,
    RetrieveUpdateDestroyAPIView,
    CreateAPIView,
    RetrieveAPIView,
)
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from django.urls import path
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny

ALL_PERMISSIONS = ["GET", "POST", "PUT", "DELETE", "PATCH"]

def get_standard_model_viewset(
    queryset,
    serializer_class,
    basic_serializer_class,
    permission_class=None,
    filter_queryset=lambda self, queryset: queryset,
):
    # Necessary because we can't have access variables of functions inside of class declaration
    class BaseContainer:
        def get_queryset():
            return queryset

        def get_serializer_class():
            return serializer_class

        def get_basic_serializer_class():
            return basic_serializer_class

        def get_permission_class():
            return permission_class

        def get_filter_queryset():
            return filter_queryset

    class AllItems(ListAPIView):
        queryset = BaseContainer.get_queryset()
        permission_class = [IsAuthenticated]
        serializer_class = BaseContainer.get_basic_serializer_class()

        def get_queryset(self):
            req_params = {}
            for key in self.request.GET.keys():
                req_params[key] = self.request.query_params.get(key)
            return BaseContainer.get_filter_queryset()(
                self, super().get_queryset(), **req_params
            )

    class AnyItem(RetrieveUpdateDestroyAPIView):
        permission_class = [
            IsAuthenticated,
            DjangoModelPermissions,
            BaseContainer.get_permission_class(),
        ]
        queryset = BaseContainer.get_queryset()
        serializer_class = BaseContainer.get_serializer_class()
        lookup_field = "id"

    class CreateItem(CreateAPIView):
        permission_class = [
            DjangoModelPermissions,
            BaseContainer.get_permission_class(),
        ]
        queryset = BaseContainer.get_queryset()
        serializer_class = BaseContainer.get_basic_serializer_class()

    class PermissionView(RetrieveAPIView):
        queryset = BaseContainer.get_queryset()
        permission_class = []

        def retrieve(self, request, *args, **kwargs):
            instance = self.get_object()
            if permission_class and hasattr(permission_class, "get_permissions"):
                return Response(permission_class.get_permissions(request, instance))

            return Response(ALL_PERMISSIONS)

    @api_view(['GET'])  
    @permission_classes([AllowAny])
    def general_permission_view(request):
        if permission_class and hasattr(permission_class, "get_general_permissions"):
            return Response(permission_class.get_general_permissions(request.user))
        return Response(ALL_PERMISSIONS)

    return [
        path("all/", AllItems.as_view()),
        path(
            "<int:id>/",
            AnyItem.as_view(),
        ),
        path(
            "create/",
            CreateItem.as_view(),
        ),
        path(
            "permissions/<int:id>/",
            PermissionView.as_view(),
        ),
        path(
            "permissions/",
            general_permission_view,
        ),
    ]
