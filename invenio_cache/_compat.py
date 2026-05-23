# SPDX-FileCopyrightText: 2017-2018 CERN.
# SPDX-License-Identifier: MIT

"""Python 2/3 compatibility module."""

from __future__ import absolute_import, print_function

import sys

PY3 = sys.version_info[0] == 3

string_types = str if PY3 else basestring
