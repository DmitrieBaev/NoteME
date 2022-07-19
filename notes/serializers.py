""" Custom serializers for note app """

from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Note, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('pk', 'notion',)
        read_only_fields = ('pk', 'notion',)


class NoteSerializer(serializers.ModelSerializer):
    # @property
    # def _user(self):
    #     request = self.context.get('request', None)
    #     if request:
    #         print('='*25)
    #         print(f'{request.user.username}')
    #         print('='*25)
    #         return request.user.username

    # created_by = serializers.PrimaryKeyRelatedField(
    #     read_only=False,
    #     queryset=User.objects.filter(username=_user),
    #     default=serializers.CurrentUserDefault()
    # )
    created_by = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    preview = serializers.ImageField(required=False)
    # categories = CategorySerializer(source='category', many=True, read_only=True)
    # category = serializers.ListSerializer(child=serializers.CharField())
    # category = serializers.SlugRelatedField(many=True, read_only=True, slug_field='notion')

    # def create(self, validated_data):
    #     category_data = validated_data.pop('category', [])
    #     note = Note.objects.create(**validated_data)
    #     for _category in category_data:
    #         ctgry = Category.objects.filter(notion=_category.get('notion'))
    #         # al.name=allergy.get('name')
    #         note.allergies.add(ctgry)
    #
    #     note.save()
    #     return note

    # def update(self, instance, validated_data):


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
