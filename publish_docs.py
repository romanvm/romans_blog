#!/usr/bin/env python
# coding: utf-8
# Author: Roman Miroshnychenko aka Roman V.M.
# E-mail: romanvm@yandex.ua
"""
Build and publish Sphinx documentation via Travis CI
"""

from __future__ import print_function
import os
import sys

if os.environ['TRAVIS_BRANCH'] != 'master' or os.environ['TRAVIS_PULL_REQUEST'] != 'false':
    print('This is not a master branch. Exiting...')
    sys.exit(0)

basedir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(basedir, 'foo'))

import romans_blog

gh_token = os.environ['GH_TOKEN']
gh_repo = 'https://{gh_token}@github.com/{repo_slug}.git'.format(gh_token=gh_token,
                                                                 repo_slug=os.environ['TRAVIS_REPO_SLUG'])
docs = os.path.join(basedir, 'docs')
html = os.path.join(docs, '_build', 'html')
os.chdir(docs)
os.system('make html')
os.chdir(html)
os.system('git init')
os.system('git config user.name "Roman Miroshnychenko"')
os.system('git config user.email "romanvm@yandex.ua"')
open('.nojekyll', 'w').close()
os.system('git add --all .')
os.system('git commit -m "Updates documentation to v.{0}"'.format(romans_blog.__version__))
os.system('git push -f -q "{gh_repo}" HEAD:gh-pages'.format(gh_repo=gh_repo))
print('Documentation published successfully.')
