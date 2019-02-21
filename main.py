import os
import csv

import pandas as pd
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session, aliased
from sqlalchemy import create_engine

from flask import Flask, jsonify, render_template,flash,redirect,url_for
from flask_sqlalchemy import SQLAlchemy

from forms import LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = 'any secret string'

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


registered_peopel=[]
csv_path="./registered_names.csv"

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    print()
    print('form.validate_on_submit()=',form.validate_on_submit())

    if form.validate_on_submit():
        flash('Login requested for user {}, {}'.format(
            form.first_name.data, form.last_name.data))
        print('flash data',form.first_name.data)
        person=dict()
        person["first_name"]=form.first_name.data
        person["last_name"]=form.last_name.data

        registered_peopel.append(person)
        with open(csv_path, 'w', newline='') as myfile:
           fieldnames = ["first_name", "last_name"] 
           writer = csv.DictWriter(myfile, fieldnames=fieldnames) 
           writer.writeheader()

           for i in range(len(registered_peopel)):
               writer.writerow({'first_name': registered_peopel[i]["first_name"], \
                   'last_name': registered_peopel[i]['last_name']})
       
    
        return render_template('login.html',form=form)
    print("hhheeeeehhehehhehehe")
    return render_template('login.html',  form=form)

@app.route("/registered_people")
def names():
    people_df=pd.read_csv(csv_path)
    people=[]
    print("people_df=", people_df)

    for index, row in people_df.iterrows():
          
          people.append({"first name": row["first_name"],"last name": row["last_name"]})
    print("people=", people)
    return   jsonify(people)


if __name__ == "__main__":
    app.run()
