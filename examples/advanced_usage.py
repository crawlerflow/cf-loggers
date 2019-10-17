import logging
from cf_loggers.elasticsearch.handler import ESLoggingHandler

logger_settings = {
    "HOSTS": ["localhost:9200"],
    "INDEX": "custom_index",
    "DOC_TYPE": "something",
    "EXTRA_DATA": {"machine_type": "task-engine"},
    "LEVEL": "INFO"
}

logging.getLogger("elasticsearch").setLevel(logging.WARNING)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s] [%(name)s]   %(message)s",
    handlers=[
        logging.StreamHandler(),
        ESLoggingHandler(
            hosts=logger_settings['HOSTS'],
            index=logger_settings['INDEX'],
            doc_type=logger_settings.get('DOC_TYPE'),
            extra_data=logger_settings.get("EXTRA_DATA", {})
        )
    ])
i = 0
while True:
    logging.info("{} Random message from random stranger".format(i))
    i += 1
