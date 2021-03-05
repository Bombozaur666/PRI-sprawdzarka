from Promela import views
from django.urls import path
from rest_framework import routers

urlpatterns = [
    path('uploadpromela/',views.task_promela_upload, name='uploadPromela'),
    path('tasklistpromela/', views.task_list_promela, name='task-list-promela'),
    path('PromelaList/', views.task_Promela_student_sended_list, name='promela-sended-list'),
    path('PromelaList/<str:file_to_open>', views.read_file_promela__task_list, name='promela-sended-task'),
    path('taskpromelaupload/',views.task_promela_upload_teacher, name='task-upload-promela'),
    path('Promela/Studentoutput/<str:file_to_open>', views.read_file_Promela_output, name='sended-promela-task'),
    path('Promela/Studentstask/<str:file_to_open>',views.read_file_Promela_task_student, name='sended-promela-output'),
    #path('task/promela/teacher_ltl/<str:file_to_open>',views.read_file_promela__task_list, name ='ltl-open')
    path('tasklistpromela/<str:file_to_open>',views.read_file_promela__task_list, name ='ltl-open')

]