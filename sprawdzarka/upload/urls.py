from upload import views
from django.urls import  path
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'students', views.StudentViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('upload/',views.task_sended_upload, name='upload'),
    path('sendedtasks/<str:file_to_open>',views.read_file1, name='sended-task'),
    path('sendedlist/',views.task_sended_list, name='sended-list'),

    path('PromelaList/', views.task_Promela_student_sended_list, name='promela-sended-list'),

    path('Promela/Studentoutput/<str:file_to_open>', views.read_file_Promela_output, name='sended-promela-task'),
    path('Promela/Studentstask/<str:file_to_open>',views.read_file_Promela_task_student, name='sended-promela-output'),

    path('tasklist/',views.task_list, name='task-list'),
    path('tasklistupload/',views.task_List_upload, name='task-list-upload'),
    path('tasklist/<str:file_to_open>',views.read_file2, name='task-list-teacher'),

    path('plagiat',views.plagiat, name='plagiat'),

    path('<str:file>', views.open_file, name='open')
]

