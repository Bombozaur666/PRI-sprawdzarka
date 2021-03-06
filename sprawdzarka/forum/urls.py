from django.urls import include, path
from .views import *


urlpatterns = [
    path('', home, name='forum'),
    path('all/', all, name='all'),
    path('<int:id>/', question, name='question'),
    path('question_choose', question_fake, name= 'add_question_choose'),
    path('answer/<int:id>/', add_answer, name = 'add_answer'),
    path('ask_question/<int:id>/', add_question, name = 'ask_question'),
]
