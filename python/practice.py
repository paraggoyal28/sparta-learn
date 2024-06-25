from pymongo import MongoClient
client = MongoClient('mongodb+srv://<user>:<password>@cluster0.cwjznmx.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
db = client.dbsparta

#find all
all_users = list(db.users.find({}, {'_id': False}))

for user in all_users:
    print(user)


#find one
user = db.users.find_one({'name': 'bobby'})

print(user)


#update record
db.users.update_one({'name': 'bobby'}, {'$set': { 'age': 19}})


#find one
user = db.users.find_one({'name': 'bobby'})

print(user)

#delete

db.users.delete_one({'name': 'bobby'})

#find one
user = db.users.find_one({'name': 'bobby'})

print(user)


