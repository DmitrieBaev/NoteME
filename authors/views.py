""" Views for authors app """

from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework.mixins import (ListModelMixin,
                                   RetrieveModelMixin,
                                   UpdateModelMixin)

from .models import Profile
from .permissions import ProfilesCustomPermissions
from .serializers import ProfileSerializer


class ProfilesViewSet(ListModelMixin,
                      RetrieveModelMixin,
                      UpdateModelMixin,
                      GenericViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (ProfilesCustomPermissions,)
    parser_classes = (MultiPartParser, FormParser, JSONParser)

    def list(self, request, *args, **kwargs):
        """
        Override get list method. Authorized user can only receive their profile info.
        """
        return Response(
            self.get_serializer(
                Profile.objects.filter(user=self.request.user),  # .select_related(User),
                many=True
            ).data
        )
