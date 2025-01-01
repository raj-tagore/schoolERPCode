# myapp/views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import AttachmentSerializer
from .models import Attachment
from rest_framework.permissions import IsAuthenticated

class AttachmentUploadView(APIView):
    
    queryset = Attachment.objects.all()
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        serializer = AttachmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
