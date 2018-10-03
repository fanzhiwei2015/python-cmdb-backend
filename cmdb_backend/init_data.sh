#!/bin/bash
set -e
username="admin"
password="Pass@1234"
email="test@gmail.com"
if [ $1 == "init" ];then
    rm db.sqlite3 || true
    rm -r cmdb/migrations/__pycache__ || true
    rm cmdb/migrations/*.py || true
    touch cmdb/migrations/__init__.py
    python manage.py makemigrations
    python manage.py migrate
    #python manage.py createsuperuser --email $email --username $username

    echo "creating user $username with password $password"

    echo "from django.contrib.auth.models import User; User.objects.create_superuser('$username', '$email', '$password')" | $PYTHON ./manage.py shell 2> /dev/null || echo "update user"


elif [ $1 == "create" ];then

    #bu
    curl -XPOST -H "Content-Type: application/json" http://127.0.0.1:8000/bus/ -d '{"name":"bu1","description":"bu1 desc"}' -u $username:$password
    curl -XPOST -H "Content-Type: application/json" http://127.0.0.1:8000/bus/ -d '{"name":"bu2","description":"bu2 desc"}' -u $username:$password
    curl -XPOST -H "Content-Type: application/json" http://127.0.0.1:8000/bus/ -d '{"name":"bu3","description":"bu3 desc"}' -u $username:$password

    #product
    curl -XPOST -H "Content-Type: application/json" http://127.0.0.1:8000/products/ -d '{"name":"product1","description":"product1 desc1","bu":"bu1"}' -u $username:$password
    curl -XPOST -H "Content-Type: application/json" http://127.0.0.1:8000/products/ -d '{"name":"product2","description":"product2 desc2","bu":"bu2"}' -u $username:$password
    curl -XPOST -H "Content-Type: application/json" http://127.0.0.1:8000/products/ -d '{"name":"product3","description":"product3 desc3","bu":"bu3"}' -u $username:$password

    #application
    curl -XPOST -H "Content-Type: application/json" http://127.0.0.1:8000/applications/ -d '{"name":"application1","description":"applications1 desc","product":"product1"}' -u $username:$password
    curl -XPOST -H "Content-Type: application/json" http://127.0.0.1:8000/applications/ -d '{"name":"application2","description":"applications2 desc","product":"product2"}' -u $username:$password
    curl -XPOST -H "Content-Type: application/json" http://127.0.0.1:8000/applications/ -d '{"name":"application3","description":"applications3 desc","product":"product3"}' -u $username:$password

    #host
    curl -XPOST -H "Content-Type: application/json" http://127.0.0.1:8000/hosts/ -d '{"name":"host1","owner":1,"ip":"10.0.0.1","description":"host1 desc","application":"application1"}' -u $username:$password
    curl -XPOST -H "Content-Type: application/json" http://127.0.0.1:8000/hosts/ -d '{"name":"host2","owner":1,"ip":"10.0.0.1","description":"host2 desc","application":"application2"}' -u $username:$password
    curl -XPOST -H "Content-Type: application/json" http://127.0.0.1:8000/hosts/ -d '{"name":"host3","owner":1,"ip":"10.0.0.1","description":"host3 desc","application":"application3"}' -u $username:$password
    curl -XPOST -H "Content-Type: application/json" http://127.0.0.1:8000/hosts/ -d '{"name":"host4","owner":1,"ip":"10.0.0.1","description":"host4 desc","application":"application3"}' -u $username:$password
    curl -XPOST -H "Content-Type: application/json" http://127.0.0.1:8000/hosts/ -d '{"name":"host5","owner":1,"ip":"10.0.0.1","description":"host5 desc","application":"application3"}' -u $username:$password

fi

####token example
#get
#curl -H  "Content-Type: application/json"  -H  "Authorization Token: 6d14b4402713a412b2543918024041621078256a" http://127.0.0.1:8000/bus/1/
#partial update
#curl -H  "Content-Type: application/json"  -H 'Authorization: Token 6d14b4402713a412b2543918024041621078256a' http://127.0.0.1:8000/bus/2/ -XPATCH -d '{"description":"bu11after pathch "}'

