import json
from typing import Any, Dict
from urllib.parse import urlencode

import requests
from requests import Response


def to_json_from_response(response: Response) -> Dict[str, Any]:
    """
    Converts the HTTP response to a JSON dictionary.

    Args:
        response (Response): The HTTP response.

    Returns:
        Dict[str, Any]: The JSON dictionary extracted from the response.
    """
    data_str = response.text.strip()
    if data_str.endswith(","):
        data_str = data_str[:-1]
    return json.loads(data_str)


def http_get(url: str, headers: Dict[str, str]) -> Response:
    """
    Performs an HTTP GET request.

    Args:
        url (str): The URL of the request.
        headers (Dict[str, str]): The headers of the request.

    Returns:
        Response: The HTTP response.
    """
    response = requests.get(
        url, headers=headers, timeout=10
    )  # Adding timeout argument with a value of 10 seconds.
    return response


def http_post(url: str, headers: Dict[str, str], data: Dict[str, Any]) -> Response:
    """
    Performs an HTTP POST request.

    Args:
        url (str): The URL of the request.
        headers (Dict[str, str]): The headers of the request.
        data (Dict[str, Any]): The data of the request.

    Returns:
        Response: The HTTP response.
    """
    response = requests.post(url, headers=headers, data=data, timeout=10)
    return response


def http_get_json(url: str, headers: Dict[str, str]) -> Dict[str, Any]:
    """
    Performs an HTTP GET request and returns the result in JSON format.

    Args:
        url (str): The URL of the request.
        headers (Dict[str, str]): The headers of the request.

    Returns:
        Dict[str, Any]: The result of the request in JSON format.
    """
    response = http_get(url, headers)
    return to_json_from_response(response)


def http_post_json(
    url: str, headers: Dict[str, str], data: Dict[str, Any]
) -> Dict[str, Any]:
    """
    Performs an HTTP POST request and returns the result in JSON format.

    Args:
        url (str): The URL of the request.
        headers (Dict[str, str]): The headers of the request.
        data (Dict[str, Any]): The data of the request.

    Returns:
        Dict[str, Any]: The result of the request in JSON format.
    """
    filtered_data = {k: v for k, v in data.items() if v is not None}
    response = http_post(url, headers, filtered_data)
    return to_json_from_response(response)


def encode_params(params: Dict[str, Any]) -> str:
    """
    Encodes the request parameters into a query string.

    Args:
        params (Dict[str, Any]): The request parameters.

    Returns:
        str: The encoded query string.
    """
    encoded_params = urlencode({k: v for k, v in params.items() if v is not None})
    return encoded_params


def url_with_params(url: str, params: Dict[str, Any]) -> str:
    """
    Adds the request parameters to the URL.

    Args:
        url (str): The URL of the request.
        params (Dict[str, Any]): The request parameters.

    Returns:
        str: The URL with the request parameters.
    """
    encoded_params = encode_params(params)
    if encoded_params:
        return f"{url}?{encoded_params}"
    else:
        return url


def catch_result(callback):
    """
    Executes a function and catches any raised exception.

    Args:
        callback: The function to execute.

    Returns:
        Any: The result of the function or None in case of exception.
    """
    try:
        return callback()
    except Exception:
        return None
