""" Custom serializers for note app """

from rest_framework import serializers

from .models import Note, Category


class NoteSerializer(serializers.ModelSerializer):
    created_by = serializers.PrimaryKeyRelatedField(
        read_only=True,
        default=serializers.CurrentUserDefault()
    )
    preview = serializers.ImageField(required=False)

    class Meta:
        model = Note
        fields = ('pk',
                  'caption',
                  'body',
                  'category',
                  'preview',
                  'is_pinned',
                  'is_public',
                  'modified_at',
                  'created_by')
        read_only_fields = ('pk', 'modified_at')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('pk', 'notion',)
        read_only_fields = ('pk', 'notion',)
