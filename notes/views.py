""" Views for notes app """

from rest_framework import generics, mixins, permissions

from .models import Note
from .permissions import IsOwnerOrPublic, IsOwner
from .serializers import NoteSerializer


class NotesList(mixins.ListModelMixin,
                mixins.CreateModelMixin,
                generics.GenericAPIView):  # generics.ListCreateAPIView
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


class NotesUpdateDestroy(mixins.DestroyModelMixin,  # generics.DestroyAPIView
                         mixins.UpdateModelMixin,   # generics.UpdateAPIView
                         generics.GenericAPIView):
    """

    """
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = (IsOwner, permissions.IsAdminUser)
















# from rest_framework.decorators import action
#
# class NoteViewSet(viewsets.ModelViewSet):
#     queryset = Note.objects.all()  # filter created_by = user
#     serializer_class = NoteSerializer
#
#     # Можно не использовать, если в настройках стоит DEFAULT_PERMISSION_CLASSES
#     # permission_classes = (permissions.IsAuthenticated,)
#     #
#     #
#     # def __init__(self, *args, **kwargs):
#     #     usr = kwargs['context']['request'].user
#     #
#     #     super(NoteViewSet, self).__init__(*args, **kwargs)
#     #     self.fields['parent'].queryset = self.get_request(usr)
#     #
#     # def get_request(self, usr):
#     #     # return Note.objects.filter(created_by=self.request.user)
#     #     return Note.objects.filter(created_by=usr)
#
#     def get_queryset(self):
#         """
#         Переопределение запроса к БД след. образом: Пользователь видит только свои заметки.
#         """
#         return Note.objects.filter(created_by=self.request.user)
#
#     @action(detail=True, methods=['get'], permission_classes=[IsOwnerOrPublic])
#     def retrieve(self, request):
#         super().retrieve(request)
#
#     @action(detail=True, methods=['put, patch'], permission_classes=[IsOwner])
#     def update(self, request, *args, **kwargs):
#         super().update(request, *args, **kwargs)
#
#     @action(detail=True, methods=['delete'], permission_classes=[IsOwner, permissions.IsAdminUser])
#     def destroy(self, request, *args, **kwargs):
#         super().destroy(request, *args, **kwargs)
