""" Views for notes app """

from rest_framework import generics, mixins, permissions

from .models import Note
from .permissions import IsOwnerOrPublic, IsOwner
from .serializers import NoteSerializer


class NotesList(mixins.ListModelMixin,
                mixins.CreateModelMixin,
                generics.GenericAPIView):
    """

    """
    serializer_class = NoteSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return Note.objects.filter(created_by=self.request.user)


class NotesRetrieve(generics.RetrieveAPIView):
    """

    """
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = (IsOwnerOrPublic,)


class NotesUpdateDestroy(mixins.DestroyModelMixin,
                         mixins.UpdateModelMixin,
                         generics.GenericAPIView):
    """

    """
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = (IsOwner, permissions.IsAdminUser)
