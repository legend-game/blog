build blog by docker
===============================
'docker build -t blog .'

run blog by docker
===============================
'docker run --name blog -d blog'

create superuser
===============================
'docker exec -it blog python /app/manage.py createsuperuser'
