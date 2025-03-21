"""to execute Python 3 code in Python 2.

redefines builtin `range` and `input` functions and `abc` either via `collections`
or `collections.abc` if available.
"""

import sys
import collections as _collections

range = range  # to allow (trivial) explicit import also in Python 3
input = input

if sys.version[0] == "2":  # in python 2
    range = xrange  # clean way: from builtins import range
    input = raw_input  # in py2, input(x) == eval(raw_input(x))
    abc = _collections  # never used

    # only for testing, because `future` may not be installed
    # from future.builtins import *
else:
    try:
        abc = _collections.abc
    except AttributeError:
        abc = _collections
