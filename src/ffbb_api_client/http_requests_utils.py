import json
from typing import Any, Dict
from urllib.parse import urlencode

import requests
from requests import Response


def to_json_from_response(response: Response) -> Dict[str, Any]:
    """
    Convertit la réponse HTTP en un dictionnaire JSON.

    Args:
        response (Response): La réponse HTTP.

    Returns:
        Dict[str, Any]: Le dictionnaire JSON extrait de la réponse.
    """
    try:
        data_str = response.text.strip()
        if data_str.endswith(","):
            data_str = data_str[:-1]
        return json.loads(data_str)
    except Exception:
        return None


def http_get(url: str, headers: Dict[str, str]) -> Response:
    """
    Effectue une requête HTTP GET.

    Args:
        url (str): L'URL de la requête.
        headers (Dict[str, str]): Les en-têtes de la requête.

    Returns:
        Response: La réponse HTTP.
    """
    response = requests.get(url, headers=headers)
    return response


def http_post(url: str, headers: Dict[str, str], data: Dict[str, Any]) -> Response:
    """
    Effectue une requête HTTP POST.

    Args:
        url (str): L'URL de la requête.
        headers (Dict[str, str]): Les en-têtes de la requête.
        data (Dict[str, Any]): Les données de la requête.

    Returns:
        Response: La réponse HTTP.
    """
    response = requests.post(url, headers=headers, data=data)
    return response


def http_get_json(url: str, headers: Dict[str, str]) -> Dict[str, Any]:
    """
    Effectue une requête HTTP GET et retourne le résultat au format JSON.

    Args:
        url (str): L'URL de la requête.
        headers (Dict[str, str]): Les en-têtes de la requête.

    Returns:
        Dict[str, Any]: Le résultat de la requête au format JSON.
    """
    response = http_get(url, headers)
    return to_json_from_response(response)


def http_post_json(
    url: str, headers: Dict[str, str], data: Dict[str, Any]
) -> Dict[str, Any]:
    """
    Effectue une requête HTTP POST et retourne le résultat au format JSON.

    Args:
        url (str): L'URL de la requête.
        headers (Dict[str, str]): Les en-têtes de la requête.
        data (Dict[str, Any]): Les données de la requête.

    Returns:
        Dict[str, Any]: Le résultat de la requête au format JSON.
    """
    filtered_data = {k: v for k, v in data.items() if v is not None}
    response = http_post(url, headers, filtered_data)
    return to_json_from_response(response)


def encode_params(params: Dict[str, Any]) -> str:
    """
    Encode les paramètres de la requête en une chaîne de requête.

    Args:
        params (Dict[str, Any]): Les paramètres de la requête.

    Returns:
        str: La chaîne de requête encodée.
    """
    encoded_params = urlencode({k: v for k, v in params.items() if v is not None})
    return encoded_params


def url_with_params(url: str, params: Dict[str, Any]) -> str:
    """
    Ajoute les paramètres de la requête à l'URL.

    Args:
        url (str): L'URL de la requête.
        params (Dict[str, Any]): Les paramètres de la requête.

    Returns:
        str: L'URL avec les paramètres de la requête.
    """
    encoded_params = encode_params(params)
    if encoded_params:
        return f"{url}?{encoded_params}"
    else:
        return url


def catch_result(callback):
    try:
        return callback()
    except Exception:
        return None
