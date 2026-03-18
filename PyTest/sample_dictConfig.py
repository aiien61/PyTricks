import logging
from logging.config import dictConfig

config = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'example': {
            'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        }
    },
    'filters': {
        'a-filter': {
            'name': 'a.b'
        }
    },
    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': 'test.log',
            'formatter': 'example',
            'filters': ['a-filter']
        }
    },
    'loggers': {
        'a': {
            'handlers': ['file'],
            'level': 'INFO',
            'propagate': True
        }
    }
}

dictConfig(config)
logger = logging.getLogger('a.b.c')
logger.debug("debug msg")
logger.info("info msg")
