#You have to create a TimedRotatingFileHandler:
# This piece of code will create a my_app.log but the log will be moved to a new log file named my_app.log.20170623 when the current day ends at midnight.

import logging
from logging.handlers import TimedRotatingFileHandler

logger = logging.getLogger('simple')

log_level = 'DEBUG'
logger.setLevel(log_level)

logfile = "time_logger.log"
# handler = TimedRotatingFileHandler(logname, when="M", interval=1) # <- toutes les minutes.
handler = TimedRotatingFileHandler(logfile, when="midnight", interval=1)
handler.suffix = "%Y%m%d.log"
formatter = logging.Formatter('%(asctime)s :: %(levelname)-8s :: [%(filename)s:%(lineno)d] :: %(message)s')
handler.setFormatter(formatter)

logger.addHandler(handler)


'''
        test code : 
'''

if __name__ == '__main__':
    logger.error("tout va bien")