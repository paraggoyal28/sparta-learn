from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient
app = Flask(__name__)

client = MongoClient('mongodb+srv://<user>:<password>@cluster0.cwjznmx.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
db = client.dbsparta
@app.route('/')
def home():
   return render_template('index.html')

@app.route("/bucket", methods=["POST"])
def bucket_post():
    bucket_receive = request.form['bucket_give']
    max_row = list(db.bucket.find({}, {'num': True, '_id': False}).sort({'num': -1}).limit(1))
    num =  max_row[0]['num'] + 1
    doc = {
        'num': num,
        'bucket': bucket_receive,
        'done': 0,
    }
    db.bucket.insert_one(doc)
    return jsonify({'msg': 'data saved successfully!'})

@app.route("/bucket/done", methods=["POST"])
def bucket_done():
    bucket_num = request.form['bucket_num']
    db.bucket.update_one({'num': int(bucket_num)}, { '$set': { 'done': 1 }})
    return jsonify({'msg': f'Updated task!'})

@app.route("/bucket/delete", methods=["POST"])
def bucket_delete():
    bucket_num = request.form['bucket_num']
    db.bucket.delete_one({'num': int(bucket_num)})
    return jsonify({'msg': f'Deleted task!'})


@app.route("/bucket", methods=["GET"])
def bucket_get():
    buckets_list = list(db.bucket.find({}, {'_id': False}))
    return jsonify({'buckets': buckets_list})

if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)