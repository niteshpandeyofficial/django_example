# django_example


#### Git Query
```bash
$ git init
$ git add .
$ git branch -M main
$ git remote add origin <git repo url>
$ git push origin main
$ git pull origin master --allow-unrelated-histories(If error occurred during merging)
```

#### Python Query

```bash
$ python freeze.

step1-Create django project 
$ django-admin startproject mysite.

step2-when we run below code then bydefault sqllite db created in folder.
python manage.py runserver

step 3-To change the port of running server
python manage.py runserver 4000(Port Number)


python manage.py createsuperuser

```


#### Create models in django

python manage.py startup service(name of model) #this snippet create folder with model and other files
add name of the model in setting.py inside installed_app section

add model details in model.py file
```bash
$ python manage.py migration
$ python manage.py migrate
```
#### add the data in admin.py and find the same details in admin portal from front end
```

