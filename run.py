__author__ = 'snwiem'

import logging
from gallery import app

HOST = '127.0.0.1'
PORT = 5000

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    app.run(host=HOST,port=PORT)