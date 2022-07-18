import math
import random
import string
from . import subapis

cc_builtins = {}

cc_builtins['string'] = string
cc_builtins['math'] = math
cc_builtins['random'] = random
cc_builtins['whrandom'] = random
cc_builtins['set'] = set
cc_builtins['frozenset'] = frozenset

cc_builtins["cc"] = subapis


def same_type(arg1, *args):
    """Compares the class or type of two or more objects."""
    t = getattr(arg1, '__class__', type(arg1))
    for arg in args:
        if getattr(arg, '__class__', type(arg)) is not t:
            return False
    return True


cc_builtins['same_type'] = same_type


def test(*args):
    length = len(args)
    for i in range(1, length, 2):
        if args[i - 1]:
            return args[i]

    if length % 2:
        return args[-1]


cc_builtins['test'] = test


def reorder(s, with_=None, without=()):
    # s, with_, and without are sequences treated as sets.
    # The result is subtract(intersect(s, with_), without),
    # unless with_ is None, in which case it is subtract(s, without).
    if with_ is None:
        with_ = s
    orig = {}
    for item in s:
        if isinstance(item, tuple) and len(item) == 2:
            key, value = item
        else:
            key = value = item
        orig[key] = value

    result = []

    for item in without:
        if isinstance(item, tuple) and len(item) == 2:
            key, ignored = item
        else:
            key = item
        if key in orig:
            del orig[key]

    for item in with_:
        if isinstance(item, tuple) and len(item) == 2:
            key, ignored = item
        else:
            key = item
        if key in orig:
            result.append((key, orig[key]))
            del orig[key]

    return result


cc_builtins['reorder'] = reorder