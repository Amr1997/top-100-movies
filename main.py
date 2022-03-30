import requests
from bs4 import BeautifulSoup

URL = 'https://www.empireonline.com/tv/features/best-tv-shows-ever-2/'

response = requests.get(URL)
website_html = response.text

soup = BeautifulSoup(website_html, 'html.parser')

all_movies = soup.findAll(name="div", class_="jsx-4245974604 listicle-item-image ")

movies_titles = [ movie.get('h3',class_='jsx-4245974604').getText() for movie in all_movies]

print(movies_titles)