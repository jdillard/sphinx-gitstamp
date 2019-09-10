Sphinx Gitstamp Generator Extension
===================================

A `Sphinx`_ extension that inserts a git datestamp into the context as
``gitstamp``, to make it available for template use in HTML versions of
your Sphinx documentation.

|Build Status| |PyPI version| |License: MIT|

Installing
----------

Directly install via pip by using::

    pip install sphinx-gitstamp

Add ``sphinx_gitstamp`` to the `extensions`_ array in your Sphinx **conf.py**.
For example::

    extensions = ['sphinx_gitstamp']

Set the value of `html_baseurl`_ in your Sphinx **conf.py** to the current
base URL of your documentation with a trailing slash. For example::

    html_baseurl = 'https://my-site.com/docs/'

See Who Is Using It
-------------------

You can use `GitHub search`_ or `libraries.io`_ to see who is using
**sphinx-sitemap**.

Contributing
------------

Pull Requests welcome! See `CONTRIBUTING`_ for instructions on how best to
contribute.

Maintaining PyPI Version
------------------------

These are the steps, to be run by the maintainer, for making a new Python
package release.

#. Rev versions in **sphinx_gitstamp/version.py** and **setup.py**.
#. Update **CHANGELOG.md**
#. Create a tag and push to GitHub::

       git tag -a vX.Y.Z -m "Release vX.Y.Z"
       git push --tags origin master

#. Create latest distribution locally::

       python setup.py sdist

#. Upload to the test pypi.org repository::

       twine upload --repository-url https://test.pypi.org/legacy/ dist/*

#. Upload to the production pypi.org repository::

       twine upload dist/*

License
-------

**sphinx-gitstamp** is made available under a **BSD license**; see `LICENSE`_ for
details.

Originally based on the gitstamp generator in the `cyrus-imapd`_ project.

.. _CONTRIBUTING: CONTRIBUTING.md
.. _cyrus-imapd: https://github.com/cyrusimap/cyrus-imapd/pull/2029/files
.. _extensions: https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-extensions
.. _GitHub search: https://github.com/search?utf8=%E2%9C%93&q=sphinx-gitstamp+extension%3Atxt&type=
.. _html_baseurl: https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-html_baseurl
.. _html_extra_path: http://www.sphinx-doc.org/en/master/usage/configuration.html#confval-html_extra_path
.. _language: https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-language
.. _libraries.io: https://libraries.io/pypi/sphinx-gitstamp
.. _LICENSE: LICENSE
.. _Sphinx: http://sphinx-doc.org/

.. |Build Status| image:: https://travis-ci.org/jdillard/sphinx-gitstamp.svg?branch=master
   :target: https://travis-ci.org/jdillard/sphinx-gitstamp
.. |PyPI version| image:: https://img.shields.io/pypi/v/sphinx-gitstamp.svg
   :target: https://pypi.python.org/pypi/sphinx-gitstamp
.. |License: MIT| image:: https://img.shields.io/badge/License-MIT-blue.svg
   :target: https://github.com/jdillard/sphinx-gitstamp/blob/master/LICENSE
