# this is python module
import numpy as np
import pandas as pd 

from flask import flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Default API"

if __name__=="__main__":
    app.run(debug=True)