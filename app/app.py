from flask import Flask, jsonify
import os
from pymongo import MongoClient
from bson.json_util import dumps
import datetime

app = Flask(__name__)

client = MongoClient(os.environ.get('DB')) 
db = client.blog

@app.route('/')
def home():
    return jsonify("please visit this url to read inserted blog post : http://0.0.0.0:5000/posts")

@app.route('/posts')
def posts():
    _items = db.posts.find({}, {'_id': False})
    return dumps(_items)

def insert():
    post = {"employee": "manaal",
    "country": "india",
    "date": datetime.datetime.utcnow()}
    post2={"employee": "abcd",
    "country": "India",
    "date": datetime.datetime.utcnow()}
    db.posts.insert_one(post)
    db.posts.insert_one(post2)

if __name__ == "__main__":
    insert()
    app.run(host='0.0.0.0', debug=True)
