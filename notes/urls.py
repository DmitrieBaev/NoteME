from django.urls import path

from . import views as v


urlpatterns = [
    # path('<int:pk>/pin', v.NoteViewSet.as_view({'get': 'list', 'post': 'create'})),
    # path('<int:pk>/unpin', v.NoteViewSet.as_view({'put': 'update', 'delete': 'destroy'}))
]
