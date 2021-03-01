from upload import views
from django.urls import path
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'students', views.StudentViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('upload/',views.task_student_sended_choose, name='upload'),
    path('uploadpromela/',views.task_promela_upload, name='uploadPromela'),
    path('uploadxml/', views.task_sended_upload, name='uploadxml'),

    path('tasklistchoose/', views.task_list_choose, name='task-list-choose'),
    path('taskuploadchoose/', views.task_upload_choose, name='task-upload-choose'),
    path('tasklistpromela/', views.task_list_promela, name='task-list-promela'),

    path('sendedtasks/<str:file_to_open>',views.read_file1, name='sended-task'),
    path('sendedlist/',views.task_sended_list, name='sended-list'),
    path('PromelaList/', views.task_Promela_student_sended_list, name='promela-sended-list'),
    path('PromelaList/<str:file_to_open>', views.read_file_promela__task_list, name='promela-sended-task'),
    path('taskpromelaupload/',views.task_promela_upload_list, name='task-upload-promela'),

    path('Promela/Studentoutput/<str:file_to_open>', views.read_file_Promela_output, name='sended-promela-task'),
    path('Promela/Studentstask/<str:file_to_open>',views.read_file_Promela_task_student, name='sended-promela-output'),

    path('tasklist/',views.task_list, name='task-list'),
    path('tasklistupload/',views.task_List_upload, name='task-list-upload'),
    path('tasklist/<str:file_to_open>',views.read_file2, name='task-list-teacher'),

    path('tasksendedchoose/', views.task_sended_choose, name='task-sended-choose'),

    path('plagiat',views.plagiat, name='plagiat'),
    path('plagiat/podglad/<str:file_to_open>', views.read_file1, name='open')
]

