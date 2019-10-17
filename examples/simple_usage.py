from cf_loggers.setup import init_logger
import logging

logger_settings = {
    "HOSTS": ["localhost:9200"],
    "INDEX": "custom_index",
    "DOC_TYPE": "something",
    "EXTRA_DATA": {"machine_type": "task-engine"},
    "LEVEL": "INFO"
}

init_logger(logger_settings)
i = 0
while True:
    logging.info("{} Random message from random stranger".format(i))
    i += 1
