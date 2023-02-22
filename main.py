import multiprocessing
import sys

# Unused standard library imports - pylint and flake8
from typing import Any, AsyncGenerator, Awaitable, Generic, Iterable, Iterator, TypeVar
from unittest.mock import Mock

# Unused own imports - pylint and flake8
import my_unused_module

# Too long line - flake8 and pylint
# A very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very long line


try:
    print(multiprocessing.cpu_count())
# Unused variable - flake8
except ImportError as exception:
    print(sys.version)
# Wrong formatting - too little space before the function's definition
# Untyped function - mypy
def foo(bar):
    return bar


# pygrep hooks: python-check-blanket-noqa
# noqa:


# pygrep hooks: python-no-eval, pylint can also detect this
eval("2 * 2")

mock = Mock()

# pygrep hooks: python-check-mock-methods
# Wrong - should be mock.assert_called_once()
assert mock.called_once()
