#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = "Josh"
SITENAME = "Josh McVey"
PORT = "8000"
SITEURL = f"http://localhost:{PORT}"
RELATIVE_URLS = True
DISPLAY_PAGES_ON_MENU = True
PATH = "content"
OUTPUT_PATH = "docs/"
TIMEZONE = "America/Chicago"
DELETE_OUTPUT_DIRECTORY = True
DEFAULT_LANG = "en"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
THEME = "simple-bootstrap"
TWITTER_USERNAME = "y3rsh"
# Blogroll
LINKS = (
    ("Pelican", "http://getpelican.com/"),
    ("Python.org", "http://python.org/"),
    ("Jinja2", "http://jinja.pocoo.org/"),
)

# Social widget
SOCIAL = (
    ("Github", "https://github.com/y3rsh"),
    ("Twitter", "https://twitter.com/y3rsh"),
    ("Instagram", "https://www.instagram.com/y3rsh/"),
    ("Linkedin", "https://www.linkedin.com/in/joshmcvey/"),
)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
STATIC_PATHS = ["images", "extra"]

EXTRA_PATH_METADATA = {
    "extra/favicon.ico": {"path": "favicon.ico"},
    "extra/CNAME": {"path": "CNAME"},
}
