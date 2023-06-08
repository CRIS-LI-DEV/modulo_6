from django.contrib import admin
from django.urls import path
from app1.views import (
    perfil_usuario,
    ingresar_datos_view,
    home,
    register,
    usuario_login,
    logout_view,carrusel
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("usuarios/", perfil_usuario, name="usuarios"),
    path("ingresar-datos/<int:user_id>/", ingresar_datos_view, name="ingresar-datos"),
    path("register/", register, name="register"),
    path("login/", usuario_login, name="login"),
    path("out/", logout_view, name="logout"),
    path("", home,name="home"),
    path("carrusel/", carrusel,name="carrusel"),
]
