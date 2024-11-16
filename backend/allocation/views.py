from rest_framework import viewsets
from .models import Classroom, Subject
from .serializers import ClassroomSerializer, SubjectSerializer
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from accounts.authentication import CookieJWTAuthentication  

class ClassroomViewSet(viewsets.ModelViewSet):
    queryset = Classroom.objects.all()
    serializer_class = ClassroomSerializer
    authentication_classes = [CookieJWTAuthentication]
    permission_classes = [IsAuthenticated, DjangoModelPermissions]
    
class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    authentication_classes = [CookieJWTAuthentication]
    permission_classes = [IsAuthenticated, DjangoModelPermissions]


