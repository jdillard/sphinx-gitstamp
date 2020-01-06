# Contributing

Thank you for your interest in contributing to **sphinx-gitstamp**!

## Process for contributing

You will need to set up a development environment to make and test your changes
before submitting them.

### Setting up a dev environment

You need to add **sphinx-gitstamp** as a
[third party extension](http://www.sphinx-doc.org/en/master/ext/thirdparty.html).

1. If your project doesn't have an extensions directory, create `exts` and
   point **conf.py** to it:

   ```sys.path.append(os.path.abspath('../exts'))```

2. Copy `sphinx_gitstamp` as a directory in your project's extensions
   directory, and rename it to `sphinx_gitstamp_dev`.

3. Add `sphinx_gitstamp_dev` to **extensions**, or change `sphinx_gitstamp` to
   `sphinx_gitstamp_dev` if you already have the extension installed via `pip`,
   in **conf.py**:

   ```extensions = ['sphinx_gitstamp_dev']```

You can now make changes to `sphinx_gitstamp_dev`.

### Testing your changes

1. Run `pycodestyle` on `sphinx_gitstamp_dev`:

   ```pycodestyle sphinx_gitstamp_dev```
