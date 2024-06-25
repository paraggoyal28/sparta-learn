from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster0.cwjznmx.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
db = client.dbsparta

#insert book records
# db.books.insert_one({
#     'title': 'Harry Potter',
#     'author': 'J.K. Rowling',
#     'rating': 90
# })

# db.books.insert_one({
#     'title': 'The Fisherman and the Fish',
#     'author': 'Joseph Choi',
#     'rating': 10
# })

# db.books.insert_one({
#     'title': 'Fire in the Water',
#     'author': 'Some Dude',
#     'rating': 57
# })

#update a record
# db.books.update_one({'title': 'The Fisherman and the Fish'}, {'$set' : {'author': 'Jimmy Kim'}})


#delete a record
# db.books.delete_one({'rating': 90})


