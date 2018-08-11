# Roman's Blog

[![Build Status](https://travis-ci.org/romanvm/romans_blog.svg?branch=master)](https://travis-ci.org/romanvm/romans_blog)
[![codecov.io](https://codecov.io/github/romanvm/romans_blog/coverage.svg?branch=master)](https://codecov.io/github/romanvm/romans_blog?branch=master)

This is a simple CMS for my blog website based on [Django](https://www.djangoproject.com/)
web-framework. It started as a learning project but then I have made this CMS
suitable for real usage.

## Main Features:

- **Post categories and "Featured" posts**: A post can (optionally) be assigned to multiple categories or marked as
  "Featured" to show it in a separate site section.
- **Disqus-powered comments and social share links** (Facebook, Linked-In, Twitter and Reddit).
- **Pages application** for creating "plain" pages that are not part of the blog and accessible via
  their own links in the site navigation menu, e.g. "About Us", "Contacts", etc.
- **WYSIWYG rich content authoring** with [TinyMCE 4](https://www.tinymce.com/) editor in admin interface.
- **Pluggable skins**: the frond-end layer is completely separated from the core code, allowing to quickly and simply
  change the site design by switching to another skin. A skin is a Django app that contains all necessary templates
  with static files (CSS, JS, fonts etc.) and (optionally) necessary template tags to render content within
  the skin context. Basically, any html site template with 1-level navigation menu can be turned into a skin.
- **Full-text site search** with [django-haystack]( http://haystacksearch.org/)
  and [Whoosh](https://pypi.python.org/pypi/Whoosh/).
- **RSS and Atom feeds** for recent blog posts.
- **SEO features**: meta description, Open Graph and schema.org metadata for posts and pages.
- **Google Analytics support**.
- **sitemap.xml and robots.txt**.
- **Localization-ready**: all interface strings, both in Python and templates, are marked as translatable.

You can see my blog CMS in action [here](http://romanvm.pythonanywhere.com/).

[Roman's Blog brief documentation](http://romanvm.github.io/romans_blog/).

**License**: [GPL v.3](http://www.gnu.org/licenses/gpl-3.0.en.html)
