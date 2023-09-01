# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.

import datetime
import os
import sys
from pathlib import Path

from sphinx.util.logging import getLogger

__version__ = "0.4.0"

logger = getLogger(__name__)

# Gets the datestamp of the latest commit on the given file
# Converts the datestamp into something more readable
# Skips files whose datestamp we can't parse.
# Expected git datestamp format: 2017-06-07 11:57:38 +1000
# Output to June 7, 2017


def page_context_handler(app, pagename, templatename, context, doctree):
    import git

    global g
    if g is None:
        # We have already errored about this
        pass

    fullpagename = Path(app.confdir, pagename)

    # Don't barf on "genindex", "search", etc
    if not os.path.isfile("%s.rst" % fullpagename):
        return

    try:
        updated = g.log("--pretty=format:%ai", "-n 1", "%s.rst" % fullpagename)
        updated = updated[:10]

        if updated == "":
            # Don't datestamp generated rst's (e.g. imapd.conf.rst)
            # Ideally want to check their source - lib/imapoptions, etc, but
            # that involves getting the source/output pair into the extension.
            return

        context["gitstamp"] = datetime.datetime.strptime(updated, "%Y-%m-%d").strftime(
            app.config.gitstamp_fmt
        )
    except git.exc.GitCommandError:
        # File doesn't exist or something else went wrong.
        logger.warning(
            "sphinx-gitstamp: Can't fetch git history for {:s}.rst.".format(pagename),
            type="gitstamp",
            subtype="file",
        )
    except ValueError:
        # Datestamp can't be parsed.
        logger.warning(
            "sphinx-gitstamp: Can't parse datestamp ({:s}), output on {:s} won't have last updated"
            "time.".format(updated, pagename),
            type="gitstamp",
            subtype="datestamp",
        )
        pass


# Only add the page context handler if we're generating html
def what_build_am_i(app):
    global g
    if app.builder.format != "html":
        return

    try:
        import git
    except ImportError:
        logger.warning(
            "sphinx-gitstamp: gitpython not found. Please ensure it is installed.",
            type="gitstamp",
            subtype="dependency",
        )
        return

    try:
        global g
        g = git.Git(".")
    except BaseException:
        logger.info(
            sys.exc_info()[0],
            type="gitstamp",
            subtype="info",
        )
        logger.warning(
            "sphinx-gitstamp: No git repository found. No git datestamps will be"
            "generated.",
            type="gitstamp",
            subtype="repo",
        )
    else:
        app.connect("html-page-context", page_context_handler)


# We can't immediately add a page context handler: we need to wait until we
# know what the build output format is.
def setup(app):
    app.add_config_value("gitstamp_fmt", "%b %d, %Y", "html")
    app.connect("builder-inited", what_build_am_i)

    return {
        "parallel_read_safe": True,
        "parallel_write_safe": True,
        "version": __version__,
    }
