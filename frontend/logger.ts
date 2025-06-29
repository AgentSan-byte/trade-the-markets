import { createLogger, format, transports } from 'winston';

// Winston logger with JSON format, ready for Splunk/Cloud SIEM integration
const logger = createLogger({
  level: 'info',
  format: format.combine(
    format.timestamp(),
    format.errors({ stack: true }),
    format.json()
  ),
  defaultMeta: { service: 'frontend' },
  transports: [
    new transports.Console()
  ]
});

export default logger;

// Usage example in any frontend file:
// import logger from './logger';
// logger.info('Frontend event', { event: 'startup', details: { ... } });

logger.info('Frontend logger initialized', { event: 'startup' });
