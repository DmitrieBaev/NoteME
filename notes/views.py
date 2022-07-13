""" Views for notes app """

from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.mixins import (ListModelMixin,
                                   CreateModelMixin,
                                   RetrieveModelMixin,
                                   UpdateModelMixin,
                                   DestroyModelMixin)

from .models import Note, Category
from .permissions import NotesCustomPermissions
from .serializers import NoteSerializer, CategorySerializer


class NotesViewSet(ListModelMixin,
                   CreateModelMixin,
                   RetrieveModelMixin,
                   UpdateModelMixin,
                   DestroyModelMixin,
                   GenericViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = (NotesCustomPermissions,)
    parser_classes = (MultiPartParser, FormParser)

    def list(self, request, *args, **kwargs):
        """
        Override get list method. Authorized user can only receive their notes.
        """
        return Response(
            self.get_serializer(
                Note.objects.filter(created_by=self.request.user),
                many=True
            ).data
        )


class CategoryReadOnlyViewSet(ListModelMixin, GenericViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAuthenticated,)
