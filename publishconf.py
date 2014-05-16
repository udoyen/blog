#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

# SITEURL = 'http://blog.jdotjdot.com'
SITEURL = 'https://jdotjdot.github.io'
RELATIVE_URLS = False

if os.getenv('HEROKU') == 'True':
    PATH = '../content' #'/app/content'
    PLUGIN_PATH = '../pelican-plugins'
    THEME = 'Gum-JJ'


FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
TAG_FEED_ATOM = 'feeds/%s.atom.xml'

# DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing

#DISQUS_SITENAME = ""
#GOOGLE_ANALYTICS = ""

