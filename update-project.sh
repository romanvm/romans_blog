#!/bin/bash

. /home/romanvm/venv39/bin/activate

cd /home/romanvm/romans_blog

git fetch
git pull

python manage.py collectstatic --noinput
python manage.py migrate
