import logging
import sys

# Configure root logger for structured output (dict-like, not JSON)
logger = logging.getLogger()
logger.setLevel(logging.INFO)
logHandler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter(
    '%(asctime)s %(levelname)s %(name)s %(message)s %(module)s %(funcName)s %(lineno)d'
)
logHandler.setFormatter(formatter)
logger.handlers = [logHandler]

# Usage example
logger.info("Backend logging initialized", extra={"event": "startup"})

# In every module, use:
# import logging
# logger = logging.getLogger(__name__)
# logger.info("Event message", extra={"event": "event_name", "details": {...}})
