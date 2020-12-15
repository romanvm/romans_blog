#!/bin/bash

. /home/romanvm/venv35/bin/activate

cd /home/romanvm/romans_blog

git fetch
git pull

python manage.py collectstatic --noinput
python manage.py migrate
