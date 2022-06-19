from django import forms
from django.contrib.auth.models import User

from .models import Note


class NoteForm(forms.ModelForm):
    """ Форма для Заметки, связанная с моделью. """
    
    # title = forms.CharField(max_length=150, title="Название")
    # # is_pinned = forms.BooleanField(default=False, verbose_name="Закреплена?")
    # category = forms.ForeignKey(Category, on_delete=models.PROTECT, verbose_name="Категория")
    # preview = forms.ImageField(upload_to='notes_preview/%Y-%m-%d/', blank=True, verbose_name="Превью")
    # body = forms.TextField(blank=True, verbose_name="Наполнение")
    # # is_deleted = forms.BooleanField(default=False, verbose_name="Удалена?")
    # # created_at = forms.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    # # updated_at = forms.DateTimeField(auto_now=True, verbose_name="Дата изменения")
    # created_by = forms.ForeignKey(to=User, on_delete=models.CASCADE, verbose_name="Автор")
    # created_by = forms.CharField(label='Автор:',
    #                              widget=forms.TextInput(attrs={'class': 'form-control form-control-sm',
    #                                                            'autocomplete': 'off',
    #                                                            'value': '{{ user.username }}'}),
    #                              required=True)
    # created_by = forms.ModelChoiceField(queryset=User.filter(username=user.username), label='Автор', empty_label=None, required=True,
    #                                     widget=forms.Select(attrs={'class': 'form-control form-control-sm'}))
    
    # def __init__(self, *args, user=None, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     if user is not None:
    #         self.fields['user'].queryset = User.objects.filter(
    #             is_active=True, username=user
    #         )
    
    def __init__( self, *args, **kwargs ):
        user = kwargs.pop('user')
        super(NoteForm, self).__init__(*args, **kwargs)
        self.fields['created_by'].queryset = User.objects.filter(username=user.username)
        self.fields['created_by'].empty_label = None
        self.fields['category'].empty_label = None
        self.fields['category'].blank = True
    
    class Meta:
        model = Note
        # fields = '__all__'  # ('title', 'body', 'category', 'preview')
        fields = ('title', 'category', 'body', 'preview', 'created_by')
        widgets = {
                'title': forms.TextInput(attrs={ 'class': 'form-control form-control-sm'}),
                'category': forms.Select(attrs={ 'class': 'form-control form-control-sm' }),
                'body': forms.Textarea(attrs={ 'class': 'form-control form-control-sm', 'rows': 25 }),
                'preview': forms.FileInput(attrs={ 'class': 'form-control form-control-sm', 'accept': '.jpg'}),
                'created_by': forms.Select(attrs={ 'class': 'form-control form-control-sm', 'hidden': 'on' })
        }
