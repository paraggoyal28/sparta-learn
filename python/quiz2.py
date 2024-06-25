from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster0.cwjznmx.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
db = client.dbsparta

# Rating of movie titled The Matrix
target_movie = db.movies.find_one({'movie': 'The Matrix'})
print(target_movie['rating'])

#Get movie titles with the same rating as the rating of 'The Matrix'
target_rating = target_movie['rating']
movies_with_same_rating = list(db.movies.find({'rating': target_rating}))
for movie in movies_with_same_rating:
    print(movie['movie'])

#Update the movie with title 'The Matrix' to have rating as 0
db.movies.update_one({'movie': 'The Matrix'}, {'$set': {'rating': 0}})

#Check for new rating
target_movie = db.movies.find_one({'movie': 'The Matrix'})
print(target_movie['rating'])
