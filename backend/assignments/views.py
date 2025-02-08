from rest_framework.viewsets import ModelViewSet
from .models import Assignment, SubmittedAssignment
from .serializers import (
    BasicAssignmentSerializer,
    AssignmentSerializer,
    SubmittedAssignmentSerializer,
)
from .permissions import AssignmentPermissions, MarkAssignmentPermissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from schoolERPCode.viewsets import get_standard_model_viewset


def assignment_filter(self, queryset, **kwargs):
    if "id" in kwargs:
        queryset = queryset.filter(id=kwargs["id"])
    if "title" in kwargs:
        queryset = queryset.filter(title__icontains=kwargs["title"])
    if "description" in kwargs:
        queryset = queryset.filter(description__icontains=kwargs["description"])
    if "is_active" in kwargs:
        queryset = queryset.filter(is_active=kwargs["is_active"])
    if "release_at" in kwargs:
        queryset = queryset.filter(release_at=kwargs["release_at"])
    if "due_at" in kwargs:
        queryset = queryset.filter(due_at=kwargs["due_at"])
    if "subject" in kwargs:
        queryset = queryset.filter(subject__id=kwargs["subject"])
    if "classroom" in kwargs:
        queryset = queryset.filter(subject__classroom__id=kwargs["classroom"])
    return queryset


assignment_viewset = get_standard_model_viewset(
    queryset=Assignment.objects.all(),
    serializer_class=AssignmentSerializer,
    basic_serializer_class=BasicAssignmentSerializer,
    permission_class=AssignmentPermissions,
    filter_queryset=assignment_filter,
)


class MarkSubmittedAssignment(ModelViewSet):
    permission_classes = [IsAuthenticated, MarkAssignmentPermissions]
    queryset = SubmittedAssignment.objects.all()
    serializer_class = SubmittedAssignmentSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()

        allowed_fields = ["status"]

        # Exclude protected fields from the update data
        data = request.data.copy()
        for field in request.data.keys():
            if field not in allowed_fields:
                data.pop(field)

        # Serialize and validate the modified data
        serializer = self.get_serializer(instance, data=data, partial=True)
        serializer.is_valid(raise_exception=True)

        # Save the instance with the modified data
        self.perform_update(serializer)

        return Response(serializer.data)

    def perform_update(self, serializer):
        serializer.save()

    def get_queryset(self):
        queryset = super().get_queryset()
        request = self.request

        id = request.query_params.get("id")
        student = request.query_params.get("student")
        assignment = request.query_params.get("assignment")
        status = request.query_params.get("status")
        submission_datetime = request.query_params.get("submission_datetime")

        if id:
            queryset = queryset.filter(id=id)
        if student:
            queryset = queryset.filter(student__id=student)
        if assignment:
            queryset = queryset.filter(assignment__id=assignment)
        if status:
            queryset = queryset.filter(status=status)
        if submission_datetime:
            queryset = queryset.filter(submission_datetime=submission_datetime)

        return queryset
