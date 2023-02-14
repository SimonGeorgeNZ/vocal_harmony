import os
from flask import Flask, render_template
from flask_pymongo import PyMongo
from bson.objectid import ObjectId


app = Flask(__name__)
# app.config["MONGO_DBNAME"] = 'CocktailTraining'
# app.config["MONGO_URI"] = 'mongodb+srv://root:Dunedin100@myfirstcluster.jekwe.mongodb.net/CocktailTraining?retryWrites=true&w=majority'

# mongo = PyMongo(app)

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()

