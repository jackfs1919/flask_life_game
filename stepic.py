#№%%
import logging
import sys

logger = logging.getLogger()
logger.setLevel(logging.INFO)
logger.addHandler(logging.StreamHandler())
logger.info("info")
logger.info(sys.path)