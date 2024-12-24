<!-- createvirtual environment --->
1. python -m venv env

step2: create gitignore file

 <!-- activate virtual environment in cmd>-->
 env\Scripts\activate

<!-- create project-->
django-admin startproject project_name .
 
<!-- Install django in terminal-->
pip install django

<!-- INSTALL requirements-->
pip freeze > requirements.txt


<!-- create app-->
<!-- python manage.py <app_name>-->
python manage.py startapp todo

<!-- run django-->
python manage.py runserver



<!-- to open python shell-->
python manage.py shell


<!-- create data in terminal-->
<Model_name>.objects.create(field1="..",field2="..",field3=".." )

<!-- Get all the data of the model-->
<Model_name>.objects.all()

<!-- Get single data of the model-->
<Model_name>.objects.get(fieldyouwanttoget = "", or id =1)

<!-- Filter data-->
<Model_name>.objects.filter(fields = "", field2 = "")

<!-- save the data-->
<Model_name>.save()

<!-- delete datal-->
<Model_name>.delete()

<!-- activate/create/add adminuser-->
python manage.py createsuperuser




