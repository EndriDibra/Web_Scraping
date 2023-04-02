# Author: Endri Dibra

# importing the required libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd


link = "https://en.wikipedia.org/wiki/The_Best_FIFA_Men%27s_Player"

link = requests.get(link).text

print(link)

soup = BeautifulSoup(link, 'lxml')

print(soup.prettify())

print(soup.title.string)

print(soup.find_all('a'))

table = soup.find_all('table')
print(table)

my_table = soup.find('table', class_='wikitable sortable')
print(my_table)

table_links = my_table.find_all('a')
print(table_links)

players = []

for links in table_links:

    players.append(links.get('title'))

print(players)

df = pd.DataFrame(players)
print(df.head())

print("Full dataset:")
print(df.to_string())