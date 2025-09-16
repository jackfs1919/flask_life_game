#№%%
import logging

log_format = "%(asctime)s--%(levelname)s--%(filename)s, " \
"line %(lineno)d, %(message)s"
logger = logging.getLogger(__name__)
# logger.setLevel(logging.INFO)
logging.basicConfig(level='DEBUG', format=log_format)
# logger.addHandler(logging.StreamHandler())
logger.info("info")