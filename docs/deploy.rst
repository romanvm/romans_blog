Deployment
==========

**Roman's Blog** is developed with Python 3.4 and Django 1.8.

Local Machine
-------------

First create and activate a clean Python 3.4-3.5 virtual environment (not mandatory but recommended).
Then clone the Github repo on your machine::

  git clone https://github.com/romanvm/romans_blog.git

Go to the project's directory::

  cd romans_blog

Install the dependencies::

  pip install -r requirements.txt

Create the DB and the admin account::

  python manage.py syncdb

Run the developement server::

  pyhton manage.py runserver

Then open http://127.0.0.1:8000 link in your browser.

You can also run ``populate_db.py`` script to populate your test site with "Lorem Ipsum" posts and pages.

To test file upload create a folder named ``media`` in the project's folder,
then create ``uploads`` sub-folder inside it.

pythonanywhere.com
------------------

`pythonanywhere.com`_ is a Python-focused web-hosting. It provides the infrastructure for simplified deploying
of Python web-apps and has a usable free plan that can be used for dev/testing or hosting a low-trafic personal page.

.. _pythonanywhere.com: https://www.pythonanywhere.com

VPS
---

**Roman's Blog** is a typical Django app so for deplyment on a VPS please follow any tutorial/manual avaliable
for deploying Django applications.
