from django.urls import include, path
from .views import *


urlpatterns = [
    path('', choose, name='forum'),

    path('home/', home, name='home'),
    path('homepromela/', home_promela, name='home_promela'),

    path('all/', all_normal, name='all_normal'),
    path('allpromela/', all_promela, name='all_promela'),

    path('<int:id>/', question, name='question'),
    path('question_choose', question_fake, name= 'add_question_choose'),

    path('promela/<int:id>/', question_promela, name='question_promela'),
    path('question_choose_promela', question_fake_promela, name='add_question_choose_promela'),

    path('answer/<int:id>/', add_answer, name = 'add_answer'),
    path('answer/promela/<int:id>/', add_answer_promela, name = 'add_answer_promela'),
    path('ask_question/<int:id>/', add_question, name = 'ask_question'),
]
