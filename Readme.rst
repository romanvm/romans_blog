Roman's Blog
============

This is a simple CMS for a blog-oriented web-site that I've developed to learn `Django`_ web-framework. Despite being
a learning project, I've tried to make this CMS suitable for real-life usage.

Main Features:
--------------

- **Post categories and "Featured" posts**: A post can (optionally) be assigned to multiple categories or marked as
  "Featured" to show it in a separate site section.
- **Disqus-powered comments and social share links** (Facebook, Linked-In, Twitter and Reddit).
- **Pages application** for creating "plain" pages that are not part of the blog and accessible via
  their own links in the site navigation menu, e.g. "About Us", "Contacts", etc.
- **WYSIWYG rich content authoring** with TinyMCE editor in admin interface. Youtube links and programming code syntax
  highlighting are supported.
- **Pluggable skins**: the frond-end layer is completely separated from the core code, allowing to quickly and simply
  change the site design by switching to another skin. Skins are Django apps that contain all the necessary templates with
  static files (CSS, JS, fonts etc.) and (optionally) the necessary template tags to render content within
  the skin context. Basically, any html site template with 1-level navigation menu can be turned into a skin.
  Skins also provide customised preview templates for TinyMCE to preview the authored content with the skin's
  styles applied. The CMS comes with 3 skins based on `Bootstrap`_ and `Bootswatch`_.
- **Full-text site search** with `django-haystack`_ and `Whoosh`_.
- **Google Analytics support**.
- **sitemap.xml and robots.txt**.
- **Localization-ready**: all interface strings, both in Python and templates, are marked as translatable.

You can see my blog CMS in action `here`_.

**License**: `GPL v.3`_

.. _Django: https://www.djangoproject.com/
.. _Bootstrap: http://getbootstrap.com/
.. _Bootswatch: http://bootswatch.com/
.. _django-haystack: http://haystacksearch.org/
.. _Whoosh: https://pypi.python.org/pypi/Whoosh/
.. _here: http://romanvm.pythonanywhere.com/
.. _GPL v.3: http://www.gnu.org/licenses/gpl-3.0.en.html
