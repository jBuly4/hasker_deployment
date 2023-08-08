#!/bin/bash
chmod 777 /hasker/wait-for-it.sh
/hasker/wait-for-it.sh db:5432
python /hasker/manage.py migrate
python /hasker/manage.py loaddata /hasker/hasker_data.json
uwsgi --ini /hasker/config/uwsgi/uwsgi.ini
