import os
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
from bson.objectid import ObjectId


app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'vocal_harmony'
app.config["MONGO_URI"] = 'mongodb+srv://root:Dunedin100@myfirstcluster.jekwe.mongodb.net/vocal_harmony?retryWrites=true&w=majority'


mongo = PyMongo(app)

@app.route('/')
def home():
    keySig = list(mongo.db.keys.find().sort("_id"))
    

    return render_template('index.html', ks=keySig)


if __name__ == '__main__':
    app.run()

