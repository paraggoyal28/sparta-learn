import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
client = MongoClient('mongodb+srv://<user>:<password>@cluster0.cwjznmx.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
db = client.dbsparta

# Read the URL and get the HTML,
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
}

# You will be scraping the data from this page
url = 'https://www.imdb.com/chart/top/?ref_=nv_mv_250'

# Use the requests library to get the HTML code at the url above
data = requests.get(url=url, headers=headers)

# The BeautifulSoup library makes it easy to
# parse HTML code
soup = BeautifulSoup(data.text, 'html.parser')

# Using select
movies = soup.select('#__next > main > div > div.ipc-page-content-container.ipc-page-content-container--center > section > div > div.ipc-page-grid.ipc-page-grid--bias-left > div > ul > li')

# Looping through the movies
for movie in movies:
    # First, let's get the title of the movie
    movie_title = movie.select_one('.ipc-title > a > h3').text
    
    #Clean movie title
    movie_title = list(movie_title.split('.'))[1].strip()
    
    # Next, let's get the year that movie was released
    year = movie.select_one('div.ipc-metadata-list-summary-item__c > div > div > div.sc-b189961a-7.feoqjK.cli-title-metadata > span:nth-child(1)').text
    # Finally, let's get the rating for each movie
    rating = movie.select_one('div.ipc-metadata-list-summary-item__c > div > div > span > div > span').text
    
    #Clean rating to remove the number of users
    rating = list(rating.split('('))[0].strip()
    
    # ...and print everything out side by side!
    print(movie_title, '/', year, '/', rating)
   
    doc = {
        'movie': movie_title,
        'year': year,
        'rating': rating
    }

    db.movies.insert_one(doc)

