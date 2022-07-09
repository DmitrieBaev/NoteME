from rest_framework import generics

from .models import Note
from .serializers import NoteSerializer


class NoteListAPIView(generics.ListAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
