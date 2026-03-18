import logging
from icecream import ic

# log rank: 10
# messages in denug mode are not allowed to output
logging.debug("debug mode message")

# log rank: 20
# messages in info mode are not allowed to output
logging.info("info mode message")

# log rank: 30
# warning mode can output messages
logging.warning("warning mode message")

# log rank: 40
# error mode can output messages
logging.error("error mode message")

# log rank: 50
# critical mode can output messages
logging.critical("critical mode message")


logformat = '%(asctime)s %(levelname)s %(message)s'
logging.basicConfig(filename="test.log",
                    level=logging.WARNING,
                    format=logformat,
                    force=True)

logging.debug("debug msg")
logging.info("info msg")
logging.warning("warning msg")