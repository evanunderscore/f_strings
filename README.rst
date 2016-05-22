f_strings
=========

Python 3.6 is getting literal string interpolation (see `PEP 498`_).
This is an imperfect backport for older Python versions.

Usage
-----

    >>> from f_strings import f
    >>> adjective = 'great'
    >>> f('f-strings are {adjective}!')
    'f-strings are great!'

Issues
------

- Uses `globals` and `locals`, so cannot access variables from closures
  (see https://www.python.org/dev/peps/pep-0498/#no-use-of-globals-or-locals)
- Uses the existing string format parser, so expressions cannot contain
  ``{``, ``}`` or ``!``.

.. _PEP 498: https://www.python.org/dev/peps/pep-0498/
