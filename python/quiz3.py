import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
url = 'https://www.billboard.com/charts/hot-100/'
data = requests.get(url,headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

songs = soup.select('#post-1479786 > div.pmc-paywall > div > div > div > div.chart-results-list > div.o-chart-results-list-row-container')

for song in songs:
    song_rank = song.select_one('ul > li.o-chart-results-list__item > span').text.strip()
    song_title = song.select_one('ul > li.lrv-u-width-100p > ul > li.o-chart-results-list__item > h3').text.strip()
    song_author = song.select_one('ul > li.lrv-u-width-100p > ul > li.o-chart-results-list__item > span').text.strip()
    print(f"{song_rank} / {song_title} / {song_author}")