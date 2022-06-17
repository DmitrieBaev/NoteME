from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


class NotesList(ListView):
    pass


class NoteDetail(DetailView):
    pass


class NoteCreate(CreateView):
    pass


class NoteUpdate(UpdateView):
    pass


class NoteDelete(DeleteView):
    pass
