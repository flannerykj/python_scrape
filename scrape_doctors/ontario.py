
# import csv
import requests
import socket
from bs4 import BeautifulSoup

def get_doctors():
    doctors_array = []
    try:
        url = 'https://www.cpso.on.ca/Public-Register-Info-(1)/Doctor-Search-Results'
        response = requests.get(url)
        html = response.content
        soup = BeautifulSoup(html, features=('html.parser'))
        print(soup)
        for item in soup.findAll('article', attrs={'class': 'doctor-search-results--result'}):
            print('item')
            print(item)
            doctors_array.append(item)
    except Exception as e:
        print(e.message)
    print(doctors_array)

get_doctors()

#outfile = open("./ontartio_doctors.csv", "wb")
#writer = csv.writer(outfile)
#writer.writerows(recipe_array)




#outfile = open("./ontartio_doctors.csv", "wb")
#writer = csv.writer(outfile)
#writer.writerows(recipe_array)
