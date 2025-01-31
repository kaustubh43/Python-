from django.urls import path

from . import views

urlpatterns = [
    path('notes', views.NoteListView.as_view(), name='notes.list'),
    path('notes/<int:pk>', views.NoteDetailView.as_view(), name='notes.details'),
    path('notes/<int:pk>/edit', views.NotesUpdateView.as_view(), name='notes.update'),
    path('notes/<int:pk>/delete', views.NotesDeleteView.as_view(), name='notes.delete'),
    path('NotFound', views.NotFoundView.as_view(), name='NotFound'),
    path('notes/new', views.NotesCreateView.as_view(), name="notes.new"),
]
