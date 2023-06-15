----------------
++++|VISTAS|++++ 
----------------
Estas vistas son pruebas de como utilizar 
las vistas.
En las vistas las principales funciones
que se crearon 
metodos de :

-registro
-logueo
-mostrar usuarios registrados
-vistas solo con logue
-carrusel


perfil_usuario(request): Obtiene perfiles de usuario
 y los muestra en la plantilla 'usuarios.html'.

ingresar_datos_view(request, user_id): Muestra el perfil
 de usuario correspondiente al user_id en la plantilla 
 'perfil_usuario.html'.

home(request): Renderiza la plantilla 'inicio.html', que es 
la página de inicio del sitio.

carrusel(request): Renderiza la plantilla 'carrusel.html'
 para mostrar un carrusel de imágenes o contenido.

register(request): Maneja el registro de usuarios, 
guarda los datos y redirige a la página de usuarios.

usuario_login(request): Maneja el inicio de sesión de
usuarios, autentica las credenciales y redirige según
 el resultado.

logout_view(request): Cierra la sesión del usuario actual
 y redirige a la página de inicio.

logueo_exitoso(request): Muestra el perfil de usuario del
usuario actual en la plantilla 'logueo_exitoso.html'
después del inicio de sesión exitoso.

galeria(request): Renderiza la plantilla 'pagina_priv_cliente.html'
 para mostrar una galería de imágenes o contenido privado.


----------------
++++|ADMIN|++++ 
----------------

 admin.site.register(PerfilDeUsuario): Registra el modelo PerfilDeUsuario
  en el panel de administración de Django.

----------------
++++|URLS|++++ 
----------------

home/: Este path se utiliza para mostrar la 
página de inicio del sitio web.

admin/: Este path se utiliza para acceder
 a la interfaz de administración del sitio web,
  proporcionada por Django.

usuarios/: Este path se utiliza para mostrar
 una lista de usuarios registrados en el sitio
  web y sus respectivos perfiles individuales.

ingresar-datos/<int:user_id>/: Este path permite 
ingresar datos relacionados con un usuario específico 
identificado por su ID. Es probable que se utilice
 para actualizar información de usuario o realizar 
 acciones específicas relacionadas con los datos
  del usuario.

register/: Este path se utiliza para mostrar el
 formulario de registro de nuevos usuarios en el
  sitio web.

login_a/: Este path se utiliza para mostrar
 el formulario de inicio de sesión de usuarios en 
 el sitio web, sin utilizar la vista predeterminada de Django LoginView.

logout/: Este path se utiliza para manejar la funcionalidad 
de cierre de sesión en el sistema.

logueo_exitoso/: Este path requiere
 que el usuario esté autenticado y muestra 
 una página de éxito después de iniciar sesión 
 correctamente.

carrusel/: Este path se utiliza para mostrar un 
carrusel de imágenes o contenido multimedia en una 
página web.

galeria/: Este path se utiliza para mostrar
 una galería de imágenes o contenido multimedia en una página web.

------------
+++Models+++ 
------------


El Modelo Perfil Usuario es basicamente una extension de la clase
user, donde se agregan algunos campos, que el modelo user que trae 
por defecto django no contempla.

-----------
+++forms+++
-----------

En este proyecto se utilizaron dos formularios
que heredan desde forms.ModelForms, no es una 
buena practica pero se estaban experimentando 
los primeros codigos con django.