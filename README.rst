Django Social Media Links
============

A reusable Django app that renders a set of social media links, i.e. for your website footer.

Installation
------------

To get the latest stable release from PyPi::

    $ pip install django-social-media-links

To get the latest commit from GitHub::

    $ pip install -e git+git://github.com/bitmazk/django-social-media-links.git#egg=social_media_links

TODO: Describe further installation steps (edit / remove the examples below):

Add ``social_media_links`` to your ``INSTALLED_APPS``::

    INSTALLED_APPS = (
        ...,
        'social_media_links',
    )

Add the ``social_media_links`` URLs to your ``urls.py``::

    urlpatterns = patterns('',
        ...
        url(r'^VAR_URL_HOOK/', include('social_media_links.urls')),
    )

Don't forget to migrate your database::

    ./manage.py migrate social_media_links


Usage
-----

TODO: Describe usage or point to docs. Also describe available settings and
templatetags.


Contribute
----------

If you want to contribute to this project, please perform the following steps::

    # Fork this repository
    # Clone your fork
    $ mkvirtualenv -p python2.7 django-social-media-links
    $ python setup.py install
    $ pip install -r dev_requirements.txt

    $ git co -b feature_branch master
    # Implement your feature and tests
    $ git add . && git commit
    $ git push -u origin feature_branch
    # Send us a pull request for your feature branch
