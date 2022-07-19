""" Custom serializers for note app """

from rest_framework import serializers

from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        default=serializers.CurrentUserDefault(),
        read_only=True
    )
    bday = serializers.DateField(required=True)
    avatar = serializers.ImageField(required=False)

    class Meta:
        model = Profile
        fields = (
            'user',
            'bday',
            'avatar',
        )
