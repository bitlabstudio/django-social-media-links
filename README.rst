Django Social Media Links
=========================

A reusable Django app that renders a set of social media links, i.e. for your
website footer.

Installation
------------

To get the latest stable release from PyPi::

    $ pip install django-social-media-links

To get the latest commit from GitHub::

    $ pip install -e git+git://github.com/bitmazk/django-social-media-links.git#egg=social_media_links

Add ``social_media_links`` to your ``INSTALLED_APPS``::

    INSTALLED_APPS = (
        ...,
        'social_media_links',
    )

Don't forget to migrate your database::

    ./manage.py migrate social_media_links

If you want to use the social icons as provided by
[monosocialfont](http://drinchev.github.io/monosocialiconsfont/) you should add
the following stylesheet to your ``base.html``::

    <head>
        <link href="{{ STATIC_URL }}social_media_links/css/styles.css" rel="stylesheet" media="screen">
    </head>
    <body>
        // Use it like so:
        <span class="symbol">&#xe224;</span>
    </body>


Usage
-----

First you need to create a set of ``LinkType`` objects. You may want to assign
symbols to them. In order to find out the codes for the symbols, please refer
to http://drinchev.github.io/monosocialiconsfont/

We provide an assignment tag that returns all social media links in your
database. You can use it like so::

    {% load social_media_links_tags %}
    {% get_social_media_links as social_media_links %}
    {% if social_media_links %}
        <ul>
            {% for link in social_media_links %}
                <li><span class="symbol">{{ link.link_type.symbol|safe }}</span><a href="{{ link.url }}" title="{{ link.title }}">{{ link.name }}</a></li>
            {% endfor %}
        </ul>
    {% endif %}

Or shorter::

    {% load social_media_links_tags %}
    {% get_social_media_links as social_media_links %}
    {% if social_media_links %}
        <ul>
            {% include "social_media_links/partials/link_list.html" with links=social_media_links %}
        </ul>
    {% endif %}


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


License
-------

This repository makes use of
[monosocialiconfonts](https://github.com/drinchev/monosocialiconsfont) so
please have a look at the license of that project.
