from django.urls import path

from . import views

app_name = 'core'

urlpatterns = [
    path('notes/', views.note_collection, name='note_collection'),
    path('note/<int:pk>/', views.note_element, name='note_element'),
]
