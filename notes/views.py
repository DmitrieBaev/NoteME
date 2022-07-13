""" Views for notes app """

from rest_framework import viewsets, mixins, response

from .models import Note
from .permissions import NotesCustomPermissions
from .serializers import NoteSerializer


class NotesViewSet(mixins.ListModelMixin,
                   mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   viewsets.GenericViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = (NotesCustomPermissions,)

    def list(self, request, *args, **kwargs):
        """
        Override get list method. Authorized user can only receive their notes.
        """
        return response.Response(
            self.get_serializer(
                Note.objects.filter(created_by=self.request.user),
                many=True
            ).data
        )
