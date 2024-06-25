import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.imdb.com/chart/top/?ref_=nv_mv_250',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

# Start coding
# tag.text
#tag['attribute']
# top tag
movies = soup.select('#__next > main > div > div.ipc-page-content-container.ipc-page-content-container--center > section > div > div.ipc-page-grid.ipc-page-grid--bias-left > div > ul > li')

for movie in movies: 
    movie_title = movie.select_one('.ipc-title > a > h3').text
    movie_year = movie.select_one('div.ipc-metadata-list-summary-item__c > div > div > div.sc-b189961a-7.feoqjK.cli-title-metadata > span:nth-child(1)').text
    movie_rating = movie.select_one('div.ipc-metadata-list-summary-item__c > div > div > span > div > span').text
    
    print(f"{movie_title} / {movie_year} / {movie_rating}")

#__next > main > div > div.ipc-page-content-container.ipc-page-content-container--center > section > div > div.ipc-page-grid.ipc-page-grid--bias-left > div
#__next > main > div > div.ipc-page-content-container.ipc-page-content-container--center > section > div > div.ipc-page-grid.ipc-page-grid--bias-left > div > ul > li:nth-child(1) > div.ipc-metadata-list-summary-item__c > div > div > div.sc-b189961a-7.feoqjK.cli-title-metadata > span:nth-child(1)
#__next > main > div > div.ipc-page-content-container.ipc-page-content-container--center > section > div > div.ipc-page-grid.ipc-page-grid--bias-left > div > ul > li:nth-child(2) > div.ipc-metadata-list-summary-item__c > div > div > span > div > span