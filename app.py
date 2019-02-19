import os

import pandas as pd
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session, aliased
from sqlalchemy import create_engine

from flask import Flask, jsonify, render_template,redirect,url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)



@app.route("/")
def index():
    """Return the homepage."""
    return render_template("index.html")


@app.route("/index_lugha")
def index_lugha():
    """Return the homepage in lugha."""
    return render_template("index_lugha.html")

@app.route("/Gallery")
def Gallery():
    """Return the homepage."""
    return render_template("Gallery.html")

if __name__ == "__main__":
    app.run()
