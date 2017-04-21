#!/bin/bash
# Update search index on pythonanywhere.com

source /home/romanvm/venv35/bin/activate
cd /home/romanvm/romans_blog
python manage.py update_index
