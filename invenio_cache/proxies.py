# SPDX-FileCopyrightText: 2017-2018 CERN.
# SPDX-License-Identifier: MIT

"""Helper proxies."""

from __future__ import absolute_import, print_function

from flask import current_app
from werkzeug.local import LocalProxy

current_cache_ext = LocalProxy(lambda: current_app.extensions["invenio-cache"])
"""Helper proxy to access cache extension object."""


current_cache = LocalProxy(lambda: current_app.extensions["invenio-cache"].cache)
"""Helper proxy to access cache object."""
