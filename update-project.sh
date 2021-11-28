#!/bin/bash

cd /home/romanvm/romans_blog

git fetch
git pull

. /home/romanvm/venv39/bin/activate

pip install -r requirements.txt

python manage.py collectstatic --noinput
python manage.py migrate
