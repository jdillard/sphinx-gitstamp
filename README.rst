Sphinx Gitstamp Generator Extension
===================================

A `Sphinx`_ extension that inserts a git datestamp into the context as
``gitstamp``, to make it available for template use in HTML versions of
your Sphinx documentation.

|PyPI version| |Downloads| |Code style: Black|

Installing
----------

Directly install via pip by using::

    pip install sphinx-gitstamp

Add ``sphinx_gitstamp`` to the `extensions`_ array in your Sphinx **conf.py**.
For example::

    extensions = ['sphinx_gitstamp']

Set the value of ``gitstamp_fmt`` in **conf.py** to the desired `time format`_.
For example::

    # Date format for git timestamps
    gitstamp_fmt = "%b %d, %Y"

Add ``gitstamp`` to the template, for example::

    {%- if gitstamp %} This page was last updated on {{ gitstamp }}. {%- endif %}

Contributing
------------

Pull Requests welcome! See `CONTRIBUTING`_ for instructions on how best to
contribute.

License
-------

**sphinx-gitstamp** is made available under a **BSD license**; see `LICENSE`_ for
details.

Originally based on the gitstamp generator in the `cyrus-imapd`_ project. This
product includes software developed by Computing Services at Carnegie Mellon
University (http://www.cmu.edu/computing/).

.. _CONTRIBUTING: CONTRIBUTING.md
.. _cyrus-imapd: https://github.com/cyrusimap/cyrus-imapd/pull/2029/files
.. _extensions: https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-extensions
.. _gitpython: https://gitpython.readthedocs.io/en/stable/
.. _html_extra_path: http://www.sphinx-doc.org/en/master/usage/configuration.html#confval-html_extra_path
.. _language: https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-language
.. _LICENSE: LICENSE
.. _Sphinx: http://sphinx-doc.org/
.. _time format: https://docs.python.org/2/library/time.html#time.strftime

.. |PyPI version| image:: https://img.shields.io/pypi/v/sphinx-gitstamp.svg
   :target: https://pypi.python.org/pypi/sphinx-gitstamp
.. |Downloads| image:: https://pepy.tech/badge/sphinx-gitstamp/month
    :target: https://pepy.tech/project/sphinx-gitstamp
.. |Code style: Black| image:: https://img.shields.io/badge/code%20style-black-000000.svg
   :target: https://github.com/psf/black
