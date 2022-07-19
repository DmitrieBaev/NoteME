""" Custom serializers for note app """

from rest_framework import serializers

from .models import Note, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('pk', 'notion',)
        read_only_fields = ('pk', 'notion',)


class NoteSerializer(serializers.ModelSerializer):
    created_by = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    preview = serializers.ImageField(required=False)
    # category field has Many2Many relationship
    # for creating or updating categories in the note
    # json request can be like:
    # {...
    # "category": [1, 13, 17],
    # ...}

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
