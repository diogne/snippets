import logging


logging.basicConfig(filename='logging_file.log', 
                    format='%(asctime)s :: %(levelname)-8s :: [%(filename)s:%(lineno)d] :: %(message)s',
                    # format='%(asctime)s :: %(levelname)s :: %(message)s', 
                    level=logging.DEBUG)

logging.debug("c'est vrai")
