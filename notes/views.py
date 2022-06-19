from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, edit

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


class NoteCreate(edit.CreateView):
    """ Контроллер создания объекта. """
    # После успешного валидирования перенаправляет на NoteDetail
    # Для работы редиректа необходим get_absolute_url в модели
    
    # self.request
    # form_class = NoteForm(user=self.request.user)
    model = Note
    form_class = NoteForm
    template_name = 'notes/note_create.html'
    
    def form_valid( self, form ):
        form.instance.created_by = self.request.user
        return super(NoteCreate, self).form_valid(form)

    # def get_queryset( self ):
    #     """ Переопределение запроса к БД. """
    #
    #     print('='*25)
    #     print(self.request.user)
    #     print('='*25)
    #
    #     return Note.objects.filter(category=self.kwargs['category_id'],
    #                                created_by=self.request.user).select_related('category')
    #
    def get_form_kwargs( self ):
        kwargs = super(NoteCreate, self).get_form_kwargs( )
        kwargs['user'] = self.request.user
        return kwargs


@login_required
def note_new(request):
    if request.method == 'POST':
        form = NoteForm(request.POST, request.FILES, user=request.user)
        if form.is_valid( ):
            form.save( )
            messages.success(request, f'Данные успешно сохранены.')
            return redirect('notes')
        else:
            messages.error(request, 'Не удалось изменить данные.')
    else:
        form = NoteForm(user=request.user)
    return render(request, 'notes/note_create.html', { "form": form })


class NoteUpdate(UpdateView):
    """ Контроллер редактирования объекта. """
    pass


class NoteDelete(DeleteView):
    """ Контроллер удаления объекта. """
    pass
