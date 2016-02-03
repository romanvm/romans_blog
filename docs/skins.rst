Skins
=====

Blog and Pages applications do not have any visual elements of their own, except for a 404 page
that is standalone and takes all CSS/JS elements from a CDN.
The site's visual appearance is completely defined by a skin.

Skin is a Django app that contains the necessary templates and (if needed) template tags.
Almost any html web-site template with 1-level navigation menu can be turned into a skin.
Roman's Blog comes with a default Cerulean skin based on based on `Bootstrap`_ and `Bootswatch`_ design elements.

A skin must provide the following templates:

- ``blog_posts_list.html`` -- used for recent posts and filtered posts lists, e.g. "Featured".
- ``blog_categories_list.html`` -- the list of post categories.
- ``blog_post.html`` -- a blog post with Disqus comments.
- ``blog_archive.html`` -- a blog archive by years and months.
- ``blog_search.html`` -- used for search results.
- ``page.html`` -- a "plain" page.
- ``tinymce_preview.html`` -- preview edited text in TinyMCE with the current skin styles applied.

.. _Bootstrap: http://getbootstrap.com/
.. _Bootswatch: http://bootswatch.com/
