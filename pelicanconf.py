#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Guillaume Gay'
SITENAME = u'Mu-Spim'
SITEURL = 'http://mu-spim.xyz'

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'fr'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_TAGS_ON_SIDEBAR = False

THEME = 'notmyidea'
BOOTSTRAP_THEME = 'flatly'

MENUITEMS = (('A DamCB project', 'http://damcb.com'),
             ('Video collection', 'https://vimeo.com/album/3550899'),)

# Blogroll
LINKS = (('DamCB', 'http://damcb.com/'),
         ('ITAV - IP3D',
          'http://http://www.itav-recherche.fr/index.php/fr/menu-itavequipeip3d/'),
         ('Foldscope', 'http://foldscope.com/'),
         ('Open-spim', 'http://openspim.org'),)

# Social widget
SOCIAL = (('tumblr', 'http://muspim.tumblr.com/'),
          ('GitHub', 'https://github.com/DamCB/mu-spim'),
          ('Twitter', 'https://twitter.com/SpimMu'),)

DEFAULT_PAGINATION = 10



# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
