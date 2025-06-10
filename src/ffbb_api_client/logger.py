import logging

logger = logging.getLogger("ffbb_api_client")


def configure_logging(level: int = logging.INFO) -> None:
    """Configure the :mod:`ffbb_api_client` logger.

    This helper attaches a simple :class:`~logging.StreamHandler` to the module
    logger and sets its level. It can be used by applications that do not have
    their own logging configuration::

        from ffbb_api_client.logger import configure_logging
        configure_logging(logging.DEBUG)

    Args:
        level: Logging level used for the logger. ``logging.INFO`` by default.
    """

    if not logger.handlers:
        handler = logging.StreamHandler()
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    logger.setLevel(level)