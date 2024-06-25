from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient

connectionStr = 'mongodb+srv://<user>:<password>@cluster0.cwjznmx.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0'
client = MongoClient(connectionStr)
db = client.dbsparta
app = Flask(__name__)

@app.route('/')
def home():
   return render_template('index.html')

@app.route("/mars", methods=["POST"])
def web_mars_post():
    name_receive = request.form['name_give']
    address_receive = request.form['address_give']
    size_receive = request.form['size_give']
    doc = {
        'name': name_receive,
        'address': address_receive,
        'size': size_receive
    }
    db.orders.insert_one(doc)
    return jsonify({'msg': 'complete!'})

@app.route("/mars", methods=["GET"])
def web_mars_get():
    orders = list(db.orders.find({}, {'_id': False}))
    return jsonify({'orders': orders})

if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)