import logging

logging.basicConfig(filename='PyLog/my_logs.log',
                    encoding='utf-8',
                    filemode='w',
                    level=logging.DEBUG,
                    format='%(levelname)s (%(asctime)s): %(message)s (Line: %(lineno)d [%(filename)s])',
                    datefmt='%d-%m-%Y %I:%M:%S %p')


logging.debug('DEBUG')
logging.info('INFO')
logging.warning('WARNING')
logging.error('ERROR')
logging.critical('CRITICAL')

x: int = 10 + 10

logging.info("The answer is: %s", x)
logging.info(f"the answer is: {x}")

import other_module
other_module.func()
