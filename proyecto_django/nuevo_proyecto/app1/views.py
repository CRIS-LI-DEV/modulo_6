from django.views.generic import View
from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse
from app1.models import PerfilDeUsuario
from .forms import UserForm,PerfilUsuarioForm,LoginUsuarioForm
from django.contrib.auth import login, authenticate,logout
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password


def perfil_usuario(request):
    usuarios = PerfilDeUsuario.objects.all()
    return render(request, 'usuarios.html', {'usuarios': usuarios})



def ingresar_datos_view(request, user_id):

        usuario = PerfilDeUsuario.objects.get(user_id=user_id)
        context = {'usuario' : usuario}
       
        return render(request, 'perfil_usuario.html', context)

def home(request):
    return render(request,'inicio.html')

def carrusel(request):
    return render(request,'carrusel.html')


def register(request):
    if request.method == 'POST':
        formulario_usuario = UserForm(request.POST)
        formulario_perfil_usuario = PerfilUsuarioForm(request.POST)
        print()
        
        if formulario_usuario.is_valid() and formulario_perfil_usuario.is_valid():
            print(formulario_usuario)
            user= formulario_usuario.save(commit=False)
            user.password= make_password(request.POST['password'])
            user.save()
           # perfil = formulario_perfil_usuario.save()
            perfil = formulario_perfil_usuario.save(commit=False)

            perfil.user=user
            perfil.save()
        
            return redirect('/usuarios/')
            
            
    
    else:
        formulario_usuario = UserForm()
        formulario_perfil_usuario=PerfilUsuarioForm()
     
    
    context = {
        'formulario_usuario': formulario_usuario,
        'formulario_perfil_usuario':formulario_perfil_usuario
        
      
        }
    
    return render(request, 'register.html', context)


def usuario_login(request):
        if request.method=='POST':
            form = LoginUsuarioForm(request.POST)
            if form.is_valid():
                usuario= form.cleaned_data['usuario']
                password = form.cleaned_data['password']
                print(usuario)
                print(password)
                user = authenticate(request, username=usuario, password=password)
                print(user)
                if user is not None:
                    if user.is_active:
                        login(request,user)
                        return  redirect('/logueo_exitoso/')
                    else:
                        return  render(request,'cuenta_desactivada.html')
                else:
                    return  render(request,'logueo_rechazada.html')
        else:
            form=LoginUsuarioForm()
        return  render(request,'login.html',{'form':form})

def logout_view(request):
    print(request.user)
    print('logout')
    logout(request)
    return redirect('/') 

 
def logueo_exitoso(request):
    print(f"logueo { request.user}")
    perfil = PerfilDeUsuario.objects.get(user_id=request.user.id)
    context={
        'perfil':perfil
    }
    return render(request,'logueo_exitoso.html',context)

def galeria(request):
    return render(request,'pagina_priv_cliente.html'  ) 