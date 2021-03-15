# boilerplateusers

crea un proyecto aparte para generar una secret_key y guardalo en un archivo .env dentro de este proyecto (desarrollo) recuerda no subir este dato a repositorios publicos 

crea tu venv, activalo y ejecuta 

´python -m venv env´
´env/Scripts/activate´
´pip install -r requirements.txt´

corre las migraciones desde la ubicacion del archivo manage.py

´python manage.py migrate'

prueba el servidor de desarrollo 

´python manage runserver´

