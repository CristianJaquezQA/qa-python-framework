# src/core/config.py
"""
Helper to read environment variables with support for:
- .env files (using python-dotenv)
- default values
- required variables
- type casting (including bool)

Usage:
    from src.core.config import env

    driver = env("DB_DRIVER")                       # string (required if no default is provided)
    server = env("DB_SERVER", r"localhost\\SQLEXPRESS")
    trusted = env("DB_TRUSTED_CONNECTION", "true")  # string
    trusted_bool = env("DB_TRUSTED_CONNECTION", False, cast=bool)  # bool
"""


import os
from typing import Any, Callable, Optional

try:
    # Carga .env si existe; no falla si no está
    from dotenv import load_dotenv, find_dotenv
    load_dotenv(find_dotenv(), override=True)
except Exception:
    # Si no está instalado python-dotenv, simplemente seguimos con os.environ
    pass


def _cast_bool(value: str) -> bool:
    """
    Convierte strings comunes a booleano.
    Verdaderos:  "1", "true", "yes", "on"
    Falsos:      "0", "false", "no", "off", ""
    """
    if value is None:
        return False
    v = str(value).strip().lower()
    if v in ("1", "true", "yes", "on"):
        return True
    if v in ("0", "false", "no", "off", ""):
        return False
    # Si viene cualquier otra cosa, considera True para no sorprender
    return True


def env(key: str,
        default: Optional[Any] = None,
        cast: Optional[Callable[[str], Any] | type] = None,
        required: bool = False) -> Any:
    """
    Lee una variable de entorno.

    :param key: nombre de la variable
    :param default: valor por defecto si no existe
    :param cast: callable o tipo al que castear (por ej. bool, int, float)
    :param required: si True y no existe la variable (ni default), lanza KeyError
    :return: valor leído (posiblemente casteado)
    """
    raw = os.getenv(key)

    if raw is None or raw == "":
        if required and default is None:
            raise KeyError(f"Missing required environment variable: {key}")
        raw = default

    # Sin cast, devuelve tal cual (útil para strings)
    if cast is None or raw is None:
        return raw

    # Casting booleano amigable
    if cast is bool:
        return _cast_bool(raw)

    # Casting genérico (int, float, list custom, etc.)
    try:
        return cast(raw)
    except Exception as exc:
        raise ValueError(f"Failed to cast env var {key!r} with value {raw!r} using {cast}: {exc}") from exc
