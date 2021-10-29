#!/bin/bash
# Update search index on pythonanywhere.com

source /home/romanvm/venv36/bin/activate
cd /home/romanvm/romans_blog
python manage.py update_index
