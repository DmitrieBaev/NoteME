""" Views for notes app """

from rest_framework import viewsets

from .models import Note
from .permissions import NotesCustomPermissions
from .serializers import NoteSerializer


class NotesViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = (NotesCustomPermissions,)
