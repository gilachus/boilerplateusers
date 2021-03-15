# boilerplateusers

código base para iniciar proyecto con user personalizado más login y signup
crea un proyecto aparte para generar una secret_key y guardalo en un archivo .env dentro de este proyecto (desarrollo) recuerda no subir este dato a repositorios publicos 

crea tu venv, activalo y ejecuta 

`python -m venv env`
`env/Scripts/activate`
`pip install -r requirements.txt`

corre las migraciones desde la ubicacion del archivo manage.py

`python manage.py migrate`

crea un super user

`python manage.py createsuperuser`

prueba el servidor de desarrollo 

`python manage runserver`

nota: esta opción es un poco problemática para hacer cambios ya que toca borrar la base de datos por ejemplo si cambias el modo de login de username a correo, o si tenias un esquema con el usuario por defecto y pasas a este personalizado la migración entra en conflicto.

