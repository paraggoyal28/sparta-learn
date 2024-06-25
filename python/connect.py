from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster0.cwjznmx.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
db = client.dbsparta

doc = {
    'name':'bob',
    'age':27
}

db.users.insert_one(doc)