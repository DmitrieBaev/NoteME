from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Note, Category
from .forms import NoteForm


class NotesList(ListView):
    """
    Контроллер показа нескольких объектов.
    ---
    Отображает все заметки пользователя.
    """
    model = Note
    context_object_name = 'notes'
    
    def get_queryset( self ):
        """
        Переопределение запроса к БД.
        По умолчанию: Model.objects.all()
        """
        
        return Note.objects.filter(created_by=self.request.user).select_related('category')


class NotesByCategoryList(ListView):
    """
    Контроллер показа нескольких объектов.
    ---
    Отображает все заметки пользователя по выбранной категории.
    """
    
    model = Note
    context_object_name = 'notes'
    allow_empty = False
    
    def get_context_data( self, *, object_list=None, **kwargs ):
        """ Добавляем дополнительные переменные в контекст. """
        
        context = super(NotesByCategoryList, self).get_context_data(**kwargs)
        context['title'] = Category.objects.get(pk=self.kwargs['category_id'])
        return context
    
    def get_queryset( self ):
        """ Переопределение запроса к БД. """
        
        return Note.objects.filter(category=self.kwargs['category_id'],
                                   created_by=self.request.user).select_related('category')


class NoteDetail(DetailView):
    """ Контроллер показа конкретного объекта. """
    # Работает благодаря get_absolute_url в модели
    model = Note
    context_object_name = 'note'


class NoteCreate(CreateView):
    """ Контроллер создания объекта. """
    # После успешного валидирования перенаправляет на NoteDetail
    # Для работы редиректа необходим get_absolute_url в модели
    
    # self.request
    # form_class = NoteForm(user=self.request.user)
    form_class = NoteForm
    template_name = 'notes/note_create.html'

    # def form_valid( self, form ):
    #     form.instance.user = self.request.user
    #     return super(NoteCreate, self).form_valid(form)

    # def get_queryset( self ):
    #     """ Переопределение запроса к БД. """
    #
    #     print('='*25)
    #     print(self.request.user)
    #     print('='*25)
    #
    #     return Note.objects.filter(category=self.kwargs['category_id'],
    #                                created_by=self.request.user).select_related('category')

    def get_form_kwargs( self ):
        kwargs = super(NoteCreate, self).get_form_kwargs( )
        kwargs['user'] = self.request.user
        return kwargs


class NoteUpdate(UpdateView):
    """ Контроллер редактирования объекта. """
    pass


class NoteDelete(DeleteView):
    """ Контроллер удаления объекта. """
    pass
