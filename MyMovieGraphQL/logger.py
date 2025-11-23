import logging
from MyMovieGraphQL import __name__ as name

class CustomFormatter(logging.Formatter):
    blue = "\x1b[0;34m"
    grey = "\x1b[38;20m"
    yellow = "\x1b[33;20m"
    red = "\x1b[31;20m"
    bold_red = "\x1b[31;1m"
    reset = "\x1b[0m"
    log_format = '%(levelname)8s %(asctime)s %(name)s.%(filename)s:%(lineno)d - %(funcName)s() - %(message)s'

    FORMATS = {
        logging.DEBUG: blue + log_format + reset,
        logging.INFO: grey + log_format + reset,
        logging.WARNING: yellow + log_format + reset,
        logging.ERROR: red + log_format + reset,
        logging.CRITICAL: bold_red + log_format + reset
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)

logger = logging.getLogger(name)
logger.setLevel(level=logging.INFO)
logger_sh = logging.StreamHandler()
logger_sh.setFormatter(CustomFormatter())
logger.addHandler(logger_sh)
