from rest_framework import serializers

from .models import Note


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ('caption', 'body', 'category', 'preview', 'is_pinned', 'is_public', 'modified_at')
