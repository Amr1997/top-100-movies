import requests
from bs4 import BeautifulSoup

URL = 'https://www.empireonline.com/tv/features/best-tv-shows-ever-2/'

response = requests.get(URL)
website_html = response.text

soup = BeautifulSoup(website_html, 'html.parser')

all_movies = soup.findAll(name="h3", class_="jsx-4245974604")

movies_titles = [ movie.getText() for movie in all_movies]

