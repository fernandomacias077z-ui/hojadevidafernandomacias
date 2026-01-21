from django.contrib import admin
from django.urls import path
from tasks import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    # --- RUTA DE INICIO ---
    path('', views.home, name='home'),
    
    # --- HOJA DE VIDA PROTEGIDA (FERNANDO) ---
    # Usamos 'profile_cv' como nombre para que coincida con tus templates
    path('profile_cv/', views.profile_cv, name='profile_cv'),

    # --- AUTENTICACIÓN ---
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('logout/', views.signout, name='logout'),

    # --- GESTOR DE TAREAS ---
    path('tasks/', views.tasks, name='tasks'),
    path('tasks_completed/', views.tasks_completed, name='tasks_completed'),
    path('tasks/create/', views.create_task, name='create_task'),
    path('tasks/<int:task_id>/', views.task_detail, name='task_detail'),
    path('tasks/<int:task_id>/complete/', views.complete_task, name='complete_task'),
    path('tasks/<int:task_id>/delete/', views.delete_task, name='delete_task'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)