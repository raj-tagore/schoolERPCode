from rest_framework.generics import (
    RetrieveUpdateDestroyAPIView,
    CreateAPIView,
)
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

def assignment_filter(self, queryset):
    request = self.request
    id = request.query_params.get("id")
    title = request.query_params.get("title")
    description = request.query_params.get("description")
    is_active = request.query_params.get("is_active")
    release_at = request.query_params.get("release_at")
    due_at = request.query_params.get("due_at")
    subject = request.query_params.get("subject")
    classroom = request.query_params.get("classroom")

    if id:
        queryset = queryset.filter(id=id)
    if title:
        queryset = queryset.filter(title__icontains=title)
    if description:
        queryset = queryset.filter(description__icontains=description)
    if is_active:
        queryset = queryset.filter(is_active=is_active)
    if release_at:
        queryset = queryset.filter(release_at=release_at)
    if due_at:
        queryset = queryset.filter(due_at=due_at)
    if subject:
        queryset = queryset.filter(subject__id=subject)
    if classroom:
        queryset = queryset.filter(subject__classroom__id=classroom)
    return queryset


assignment_viewset = get_standard_model_viewset(
    queryset=Assignment.objects.all(),
    serializer=AssignmentSerializer,
    basic_serializer=BasicAssignmentSerializer,
    permission=AssignmentPermissions,
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
