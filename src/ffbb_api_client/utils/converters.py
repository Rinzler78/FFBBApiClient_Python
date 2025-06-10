"""
Data conversion utilities for FFBB API responses.

This module provides type-safe converters for transforming JSON data from FFBB API
responses into Python objects. These functions handle type validation, conversion,
and error handling for various data types.

The converters are designed to work with the deserialization process, ensuring
that API response data is properly validated and converted to the expected types.
"""

from datetime import datetime
from typing import Any, Callable, List, Type, TypeVar, cast

import dateutil.parser

T = TypeVar("T")


def from_none(x: Any) -> Any:
    """
    Validate that a value is None.

    Args:
        x: Value to validate.

    Returns:
        The input value if it is None.

    Raises:
        AssertionError: If x is not None.
    """
    assert x is None
    return x


def from_str(x: Any) -> str:
    """
    Convert and validate a value as a string.

    Args:
        x: Value to convert to string.

    Returns:
        The validated string value.

    Raises:
        AssertionError: If x is not a string.
    """
    assert isinstance(x, str)
    return x


def from_union(fs, x):
    """
    Try multiple conversion functions until one succeeds.

    This function attempts to convert a value using a list of converter functions,
    returning the result from the first function that doesn't raise an exception.

    Args:
        fs: List of converter functions to try.
        x: Value to convert.

    Returns:
        The converted value from the first successful converter.

    Raises:
        AssertionError: If all conversion functions fail.
    """
    for f in fs:
        try:
            return f(x)
        except Exception:
            pass
    assert False


def from_float(x: Any) -> float:
    """
    Convert and validate a value as a float.

    Args:
        x: Value to convert to float. Can be int or float, but not bool.

    Returns:
        The converted float value.

    Raises:
        AssertionError: If x is not a numeric type or is a boolean.
    """
    assert isinstance(x, (float, int)) and not isinstance(x, bool)
    return float(x)


def is_type(t: Type[T], x: Any) -> T:
    """
    Validate that a value is of a specific type.

    Args:
        t: Expected type.
        x: Value to validate.

    Returns:
        The input value cast to the expected type.

    Raises:
        AssertionError: If x is not an instance of type t.
    """
    assert isinstance(x, t)
    return x


def to_float(x: Any) -> float:
    """
    Validate that a value is already a float.

    Args:
        x: Value to validate as float.

    Returns:
        The validated float value.

    Raises:
        AssertionError: If x is not a float.
    """
    assert isinstance(x, float)
    return x


def from_int(x: Any) -> int:
    """
    Convert and validate a value as an integer.

    Args:
        x: Value to validate as integer. Must be int, not bool.

    Returns:
        The validated integer value.

    Raises:
        AssertionError: If x is not an integer or is a boolean.
    """
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def from_stringified_bool(x: str) -> bool:
    """
    Convert a string representation of a boolean to a boolean value.

    Args:
        x: String to convert. Must be "true" or "false".

    Returns:
        True if x is "true", False if x is "false".

    Raises:
        AssertionError: If x is not "true" or "false".
    """
    if x == "true":
        return True
    if x == "false":
        return False
    assert False


def from_datetime(x: Any) -> datetime:
    """
    Convert a string to a datetime object.

    Uses dateutil.parser to handle various datetime string formats commonly
    found in API responses.

    Args:
        x: String representation of a datetime.

    Returns:
        Parsed datetime object.

    Raises:
        ParserError: If the string cannot be parsed as a datetime.
    """
    return dateutil.parser.parse(x)


def to_class(c: Type[T], x: Any) -> dict:
    """
    Convert an object to its dictionary representation.

    Args:
        c: Expected class type.
        x: Object to convert, must be an instance of class c.

    Returns:
        Dictionary representation of the object via its to_dict() method.

    Raises:
        AssertionError: If x is not an instance of class c.
    """
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


def from_bool(x: Any) -> bool:
    """
    Validate that a value is a boolean.

    Args:
        x: Value to validate as boolean.

    Returns:
        The validated boolean value.

    Raises:
        AssertionError: If x is not a boolean.
    """
    assert isinstance(x, bool)
    return x


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    """
    Convert a list by applying a converter function to each element.

    Args:
        f: Converter function to apply to each list element.
        x: List to convert.

    Returns:
        New list with converted elements.

    Raises:
        AssertionError: If x is not a list.
    """
    assert isinstance(x, list)
    return [f(y) for y in x]
