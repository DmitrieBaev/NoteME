""" Custom serializers for note app """

from rest_framework import serializers

from .models import Note


class NoteSerializer(serializers.ModelSerializer):
    # created_by = serializers.PrimaryKeyRelatedField(
    #     read_only=True,
    #     default=serializers.CurrentUserDefault()
    # )

    class Meta:
        model = Note
        fields = ('pk',
                  'caption',
                  'body',
                  'category',
                  # 'preview',
                  'is_pinned',
                  'is_public',
                  'modified_at',
                  'created_by')
        read_only_fields = ('pk', 'modified_at')

    # def validate(self, attrs):
    #     attrs = super().validate(attrs)
    #     attrs['caption'] = self.context['request'].data['caption']
    #     attrs['body'] = self.context['body']
    #     attrs['category'] = self.context['category']
    #     # attrs['preview'] = self.context['preview']
    #     attrs['is_pinned'] = self.context['is_pinned']
    #     attrs['is_public'] = self.context['is_public']
    #     return attrs
