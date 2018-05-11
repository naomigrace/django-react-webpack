from django.urls import path

from .views import PollQuestions, index


urlpatterns = [
    path('', index, name='index'),
    path('questions/', PollQuestions.as_view(), name='questions')
]