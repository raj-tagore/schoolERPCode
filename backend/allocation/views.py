from rest_framework import viewsets
from .models import Classroom, Subject
from .serializers import ClassroomSerializer, SubjectSerializer, BasicClassroomSerializer
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from rest_framework.generics import RetrieveUpdateDestroyAPIView, RetrieveAPIView, ListAPIView, CreateAPIView
from .permissions import ClassroomPermissions, SubjectPermissions

class AllClassrooms(ListAPIView):
    queryset = Classroom.objects.all()
    serializer_class = BasicClassroomSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = super().get_queryset()
        request = self.request

        id = request.query_params.get('id')
        name = request.query_params.get('name')
        standard = request.query_params.get('standard')
        class_teacher = request.query_params.get('class_teacher')

        if id:
            queryset = queryset.filter(id=id)
        if name:
            queryset = queryset.filter(name__icontains=name)
        if standard:
            queryset = queryset.filter(standards__id=standard)
        if class_teacher:
            queryset = queryset.filter(class_teacher__id=class_teacher)

        return queryset

class AnyClassroom(RetrieveUpdateDestroyAPIView):
    serializer_class = ClassroomSerializer
    permission_classes = [IsAuthenticated, ClassroomPermissions]
    queryset = Classroom.objects.all()
    lookup_field = 'id'

class CreateClassroom(CreateAPIView):
    queryset = Classroom.objects.all()
    serializer_class = ClassroomSerializer
    permission_classes = [DjangoModelPermissions]


class AllSubjects(ListAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = super().get_queryset()
        request = self.request

        id = request.query_params.get('id')
        name = request.query_params.get('name')
        is_active = request.query_params.get('is_active')
        description = request.query_params.get('description')
        classroom = request.query_params.get('classroom')
        main_teacher = request.query_params.get('main_teacher')


        if id:
            queryset = queryset.filter(id=id)
        if name:
            queryset = queryset.filter(name__icontains=name)
        if is_active:
            queryset = queryset.filter(is_active=is_active)
        if description:
            queryset = queryset.filter(description__icontains=description)
        if classroom:
            queryset = queryset.filter(classroom__id=classroom)
        if main_teacher:
            queryset = queryset.filter(main_teacher__id=main_teacher)

        return queryset

class AnySubject(RetrieveUpdateDestroyAPIView):
    serializer_class = SubjectSerializer
    permission_classes = [IsAuthenticated, SubjectPermissions]
    queryset = Subject.objects.all()
    lookup_field = 'id'

class CreateSubject(CreateAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    permission_classes = [DjangoModelPermissions]

