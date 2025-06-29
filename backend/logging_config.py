import logging
import sys
from pythonjsonlogger import jsonlogger

# Configure root logger for structured JSON output
logger = logging.getLogger()
logger.setLevel(logging.INFO)
logHandler = logging.StreamHandler(sys.stdout)
formatter = jsonlogger.JsonFormatter(
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
