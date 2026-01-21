from django.contrib import admin
from django.urls import path
from tasks import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('logout/', views.signout, name='logout'),
    path('profile/', views.profile_cv, name='profile_cv'),
    path('projects/', views.tasks, name='tasks'),
    path('projects/create/', views.create_task, name='create_task'),
    path('projects/<int:task_id>/', views.task_detail, name='task_detail'),
]