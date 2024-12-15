from rest_framework import viewsets
from .models import Classroom, Subject
from .serializers import ClassroomSerializer, SubjectSerializer
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions

class ClassroomViewSet(viewsets.ModelViewSet):
    queryset = Classroom.objects.all()
    serializer_class = ClassroomSerializer
    permission_classes = [DjangoModelPermissions]
    
class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    permission_classes = [DjangoModelPermissions]


