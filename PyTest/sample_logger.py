import logging

logger = logging.getLogger("a.b.c")
logger.setLevel(logging.INFO)

handler = logging.FileHandler('test.log')
handler.setLevel(logging.INFO)

filter = logging.Filter('a.b')

formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

handler.setFormatter(formatter)
handler.addFilter(filter)
logger.addHandler(handler)
logger.addFilter(filter)

logger.debug("debug msg")
logger.info("info msg")
