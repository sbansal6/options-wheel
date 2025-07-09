import logging as log
import sys
from pathlib import Path

def setup_logger(log_file="logs/run.log", level="INFO", to_file=False):
    logger = log.getLogger("strategy")
    logger.setLevel(getattr(log, level.upper()))

    if not logger.handlers:
        # Console output
        ch = log.StreamHandler(sys.stdout)
        ch.setLevel(getattr(log, level.upper()))
        ch.setFormatter(log.Formatter("[%(message)s]"))
        logger.addHandler(ch)

        # File output
        if to_file:
            Path(log_file).parent.mkdir(parents=True, exist_ok=True)
            fh = log.FileHandler(log_file)
            fh.setLevel(log.DEBUG)
            fh.setFormatter(log.Formatter(
                "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
            ))
            logger.addHandler(fh)

    return logger
