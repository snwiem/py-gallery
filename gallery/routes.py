__author__ = 'snwiem'

import logging
from flask import render_template
from gallery import app

@app.route('/')
def index():
    logging.debug("BEGIN")
    return render_template("index.html")