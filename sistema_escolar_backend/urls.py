from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views.bootstrap import VersionView
from sistema_escolar_backend.views import users
from sistema_escolar_backend.views import auth
from sistema_escolar_backend.views import alumnos
from sistema_escolar_backend.views import maestros

urlpatterns = [
    # Create Admin
    path('admin/', users.AdminView.as_view()),
    # Create Alumno
    path('alumnos/', alumnos.AlumnosView.as_view()),
    # Create Maestro
    path('maestros/', maestros.MaestrosView.as_view()),
    # Login
    path('login/', auth.CustomAuthToken.as_view()),
    # Logout
    path('logout/', auth.Logout.as_view())
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
