[![Build Status](https://travis-ci.org/CSnap/Django-pre-post.svg?branch=master)](https://travis-ci.org/CSnap/Django-pre-post)

# Django-pre-post
This Django app provides the ability to create pre-post questions and answers. It was developed by the CSDTs team at RPI to embed pre-post tests for students in their website and to ease data collection.

# Installation

## Download and install:
Either use pip in terminal: `pip install django_pre_post`
Or add django_pre_post to your requirements / libraries file and run `pip install -r requirements.txt`

## Add the application to your site:
Include it in settings.py
```
INSTALLED_APPS = (
    ... your apps here ...
    'django_pre_post',
)
```
Include it in URLS.py
```
urlpatterns = [
    ... your pages here...
    url(r'^questionnaire/', include('django_pre_post.urls')),
]
```