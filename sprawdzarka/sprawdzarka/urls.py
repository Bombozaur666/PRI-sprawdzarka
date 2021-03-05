from django.contrib import admin
from django.urls import path, include
from users import views as user_views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', user_views.register, name='register'),
    path('profile/', user_views.profile, name='profile'),
    path('grupy/',user_views.groups, name = 'all_groups'),
    path('grupy/<str:group_id>',user_views.all_students, name = 'group'),
    path('nowa_grupa',user_views.new_group, name = 'new_group'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('', include('api.urls')),
    path('task/', include('upload.urls')),
    path('promela/', include('Promela.urls')),
    path('forum/', include('forum.urls')),
    path('tests/',include('tests.urls')),
]
