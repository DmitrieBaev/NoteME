""" Views for notes app """

from rest_framework import generics, mixins, permissions, viewsets

from .models import Note
from .permissions import NotesCustomPermissions
from .serializers import NoteSerializer


class NotesViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = (NotesCustomPermissions,)

# class NotesViewSet(mixins.ListModelMixin,
#                    mixins.CreateModelMixin,
#                    mixins.RetrieveModelMixin,
#                    mixins.UpdateModelMixin,
#                    mixins.DestroyModelMixin,
#                    generics.GenericAPIView):
#     """
#     Custom view, that provides:
#     - list
#     - create
#     - retrieve
#     - update = partial_update (the same here)
#     - destroy
#     """
#     serializer_class = NoteSerializer
#
#     def get_queryset(self):
#         """
#         Determine the request for DB
#         """
#         return Note.objects.filter(created_by=self.request.user)
#
#     # @classmethod
#     # def get_extra_actions(cls):
#     #     return []
#
#     def get_permissions(self):
#         """
#         Instantiates and returns the list of permissions for different endpoints that this view requires.
#         """
#         # if self.action in ['list', 'create']:
#         #     permission_classes = (permissions.IsAuthenticated,)
#         if self.action == 'retrieve':
#             permission_classes = (IsOwnerOrPublic, permissions.IsAdminUser)
#         if self.action in ['update', 'partial_update', 'destroy']:
#             permission_classes = (IsOwner,)
#         return [permission() for permission in permission_classes]
#
#     def put(self, request, format=None, *args, **kwargs):
#         """
#         Overriding update method in such a way that UPDATE and PARTIAL_UPDATE are the same
#         """
#         return self.partial_update(request, *args, **kwargs)



















# class NotesListCreate(generics.ListCreateAPIView):
#     """
#
#     """
#     serializer_class = NoteSerializer
#     permission_classes = (permissions.IsAuthenticated,)
#
#     def get_queryset(self):
#         return Note.objects.filter(created_by=self.request.user)





# class NotesList(mixins.ListModelMixin,
#                 mixins.CreateModelMixin,
#                 generics.GenericAPIView):
# class NotesList(generics.ListCreateAPIView):
#     """
#
#     """
#     serializer_class = NoteSerializer
#     permission_classes = (permissions.IsAuthenticated,)
#
#     def get_queryset(self):
#         return Note.objects.filter(created_by=self.request.user)
#
#




# class NotesRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
#     """
#     Provides next actions on ^/prefix/id/ endpoint:
#     - retrieve (get)
#     - update = partial_update (put, patch <the same>)
#     - destroy (delete)
#     """
#     queryset = Note.objects.all()
#     serializer_class = NoteSerializer
#     permission_classes = (NotesCustomPermissions,)
#
#     def put(self, request, *args, **kwargs):
#         """
#         Overriding update method in such a way that UPDATE and PARTIAL_UPDATE are the same
#         """
#         return self.partial_update(request, *args, **kwargs)




# class NotesRetrieve(generics.RetrieveAPIView):
#     """
#
#     """
#     queryset = Note.objects.all()
#     serializer_class = NoteSerializer
#     permission_classes = (IsOwnerOrPublic,)
#
#
# class NotesUpdateDestroy(mixins.DestroyModelMixin,
#                          mixins.UpdateModelMixin,
#                          generics.GenericAPIView):
# # class NotesUpdateDestroy(generics.UpdateAPIView,
# #                          generics.DestroyAPIView):
#     """
#
#     """
#     queryset = Note.objects.all()
#     serializer_class = NoteSerializer
#     permission_classes = (IsOwner, permissions.IsAdminUser)
#
#     def put(self, request, *args, **kwargs):
#         return self.partial_update(request, *args, **kwargs)
#
#     def perform_destroy(self, instance):
#         instance.delete()
