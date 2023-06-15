from django.contrib import admin
from django.urls import path
from app1.views import (
    perfil_usuario,
    ingresar_datos_view,
    home,
    register,
    usuario_login,
    logout_view,carrusel,logueo_exitoso,galeria
)
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path("", home,name="home"),
    path("admin/", admin.site.urls),
   #LISTAR USUARIOS Y PERFIL INDIVIDUAL
    path("usuarios/", perfil_usuario, name="usuarios"),
    path("ingresar-datos/<int:user_id>/", ingresar_datos_view, name="ingresar-datos"),
    
    path("register/", register, name="register"),
    #LOGINS SIN LOGINVIEW
    path("login_a/", usuario_login, name="login_sin_login_view"),
   path("logout_a/", logout_view, name="logout_sin_login_view"),
    #LOGINS
    path("login/",LoginView.as_view(template_name='login_view.html'),name="login_login_view"),
    path("logout/",LogoutView.as_view(),name="login_login_view"),
    path('logueo_exitoso/',login_required(logueo_exitoso),name='logueo_exitoso' ),
    #PRUEBA DE CARRUSEL   
    path("carrusel/", carrusel,name="carrusel"),
    path("galeria/", galeria,name="galeria"),
    
 
]