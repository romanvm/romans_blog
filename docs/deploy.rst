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

Login into the admin panel, open "Sites" section and enter ``127.0.0.1:8000`` as **Domain name**
(**Display name** can be any). This is needed so that links from the admin panel to your site pages work properly.

You can also run ``populate_db.py`` script to populate your test site with "Lorem Ipsum" posts and pages.

To test file upload create a folder named ``media`` in the project's folder,
then create ``uploads`` sub-folder inside it.

VPS
---

**Roman's Blog** is a typical Django app so for deployment on a VPS please follow any tutorial/manual available
for deploying Django applications. But there are a couple of things you need to note.

Create a folder that will be served by your web-sever under ``/media/`` path.
Then create a sub-folder ``/uploads/`` inside it. This subfolder must be accessible for writing to the web-server
user.

By default the main project's ``settings.py`` module tries to import ``local_settings.py`` module with production
settings. So you must create such file along with the main ``settings.py``. As the absolute minimum,
``local_settings.py`` must define your production ``SECRET_KEY`` and ``DATABASES`` variables. You can use
`Django Secret Key Generator`_ to generate a new secret key.

Modern best practices, like `Two Scoops of Django`_, consider defining your production settings in a non-versioned
``local_settings.py`` as an "anti-pattern", but in my opinion that is too harsh and using a "local" Python
module for defining production settings is OK for small projects like this with only a few production settings that
need to be kept secret.

Don't forget to set ``DEBUG = False`` and define ``ALLOWED_HOSTS`` for your site.
Also set **Domain name** in the admin panel (see above) to your site's actual domain name.

To enable `Disqus`_ comments for posts and Google Analytics tracking define ``DISQUS_SHORTNAME``
and ``GOOGLE_ANALYTICS_ID`` variables in the project's ``settings.py`` respectively.

To update ``django-haystack`` search index you need either to define
``HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'`` in the project's ``settings.py``
(if your server has enough CPU power to run indexing on every save) or to schedule
``python manage.py update_index`` command to run at regular intervals.

.. _Django Secret Key Generator: http://www.miniwebtool.com/django-secret-key-generator/
.. _Two Scoops of Django: http://www.amazon.com/Two-Scoops-Django-Best-Practices/dp/0981467342
.. _Disqus: https://disqus.com/
