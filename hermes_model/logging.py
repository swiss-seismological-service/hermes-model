try:
    from prefect.logging import get_run_logger
    PREFECT = True
except ImportError:
    import logging
    PREFECT = False


def get_logger():
    if PREFECT:
        logger = get_run_logger()
    else:
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.INFO)
    return logger
