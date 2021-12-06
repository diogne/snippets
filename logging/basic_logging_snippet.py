"""


cf. tuto officiel : https://docs.python.org/fr/3/howto/logging.html

Pour un usage plus avancé : https://docs.python.org/fr/3/howto/logging-cookbook.html#logging-cookbook

"""

import logging


logging.basicConfig(filename='logging_file.log', 
                    format='%(asctime)s :: %(levelname)-8s :: [%(filename)s:%(lineno)d] :: %(message)s',
                    # format='%(asctime)s :: %(levelname)s :: %(message)s', 
                    level=logging.DEBUG)



logging.debug("c'est vrai")
logging.warning('Watch out!')  # will print a message to the console
