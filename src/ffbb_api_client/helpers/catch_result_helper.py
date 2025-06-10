import json

from requests.exceptions import ConnectionError, ReadTimeout


class CatchResultError(Exception):
    """Raised when ``catch_result`` fails to execute the callback."""


def catch_result(callback, is_retrieving: bool = False):
    """
    Catch the result of a callback function.

    Args:
        callback: The callback function.

    Returns:
        The result of the callback function or ``None`` if a JSON decoding error
        occurs.

    Raises:
        CatchResultError: If ``callback`` raises an unexpected exception.
    """

    try:
        return callback()
    except json.decoder.JSONDecodeError as e:
        if e.msg == "Expecting value":
            return None
        raise e
    except ReadTimeout as e:
        if not is_retrieving:
            return catch_result(callback, True)
        raise e
    except ConnectionError as e:
        if not is_retrieving:
            return catch_result(callback, True)
        raise e
    except Exception as e:
        raise CatchResultError(str(e)) from e
