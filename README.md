# real-estate
real estate listing application


https://www.django-rest-framework.org/tutorial/quickstart/
https://blog.logrocket.com/django-rest-framework-create-api/


pip install django
pip install django_rest_framework
python manage.py createsuperuser

http://127.0.0.1:8000/admin/
http://127.0.0.1:8000/todos/api
http://127.0.0.1:8000/todos/api/<id>/


# Add new items
curl -v -u admin:admin http://127.0.0.1:8000/api/todos | jq .
curl -v -u admin:admin -X POST -H 'Content-Type: application/json' http://127.0.0.1:8000/api/todos -d '{"task": "New Task1","completed": false}' | jq .



curl -u krish:djangoadmin -X POST -H 'Content-Type: application/json' http://127.0.0.1:8000/api/todos -d '{"task": "New Task1","completed": false}' | jq .


# sqlite3 commands
```
sqlite3 todo/db.sqlite3
.tables
SELECT * FROM table
```

#passwords
admin/admin
krish/djangoadmin