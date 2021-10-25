# Desarollo de sistemas 

Equipo:
Casareski, Juan I.

Keberlein, Gian.

Fontanazzi, Valentino.



### Manual de usuario:
Al entrar al index de la página se encontrará con un menu el cual posee 2 hipervínculos, el primero para registrarse y el otro para iniciar sesión.

Para registrarse se debe ingresar su nombre de usuario, contraseña y email. 
Luego debera iniciar sesion en la pagina de login con su cuenta registrada.

Una vez conectado se le permitira acceder a la lista de barrios accediendo desde el boton en la izquina superior derecha.

Dentro del mismo al iniciar por primera vez debera rellenar un formulario indicando la provincia y el barrio a buscar.
Ya con la lista podra acceder a la información detallada de cada barrio, en la cual también podra asignarle los paquetes a cada barrio.

Tambien podra acceder al apartado de estadisticas en el apartado de la esquina superior izquierda.

Librerias utilizadas: 
flask
werkzeug.exceptions
werkzeug.user_agent
werkzeug.security
wtforms
wtforms.fields.html5




#### Notas:

http://127.0.0.1:5000/login es la pagina de inicio, no hacer caso a el url '/'

Una vez logueado hay q tocar en el segundo icono de la navbar

Despues escribir la provincia y localidad y se mostrara la lista de barrios

Por la razon q sea el boton a la derecha de cada barrio no funciona, asi q hay que escribire el url a mano (poniendo /Tolosa para tolosa)

Ahí se puede poer el numero de paquetes y darle a agregar, pero el numero de paquetes se actualiza un clic tarde

En el 3er icono  (unas barras verticales) hay q  solucionar el formato.