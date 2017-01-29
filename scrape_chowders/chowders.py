
import csv
import requests 
import socket
from bs4 import BeautifulSoup
from parse_ingredient.en import parse

print parse_ingredient.en

"""recipe_array = []
def get_chowder_urls():
    chowder_urls = []
    for i in range(1, 8):      # Number of pages plus one 
        try: 
            url = 'http://www.epicurious.com/search/chowder?page=%d' % i
            response = requests.get(url)
            html = response.content
            soup = BeautifulSoup(html)
            h4s_list = soup.findAll('h4', attrs={'class': 'hed'})
            for item in h4s_list:
                item_name = item.find('a').text
                item_url = 'http://www.epicurious.com'+item.find('a').get('href')
                chowder_urls.append(item_url)
        except Exception as e:
            print (e.message)
    return chowder_urls

def get_ingredients(url):  
    ingredient_array = [] 
    try: 
        response = requests.get(url)
        html = response.content
        soup = BeautifulSoup(html)
        ingredient_title = soup.find('h1', attrs={'itemprop': 'name'}).text
        ingredient_ul = soup.find('ul', attrs={'class': 'ingredients'})
        ingredient_array.append(ingredient_title.encode())
        for item in ingredient_ul.findAll('li'):
            text = item.text.encode()
            parsed = parse(text)["name"]
            ingredient_array.append(parsed)
    except Exception as e:
        print (e.message)
    return ingredient_array

def compile_recipes(url_array):
    recipe_array = []
    for url in url_array:      # Number of pages plus one 
        try: 
            recipe_array.append(get_ingredients(url))
        except Exception as e:
            print (e.message)
    return recipe_array

def clean_ingredient(text):
    chars_to_remove = ['1/4', '!', '?']
    result = parse(text)["name"]
    result.translate(None, ''.join(chars_to_remove))
    return result

chowder_urls = get_chowder_urls()
recipe_array = compile_recipes(chowder_urls)

outfile = open("./epicurious-chowders.csv", "wb")
writer = csv.writer(outfile)
writer.writerows(recipe_array) """

text = "1/4-inch cubes fresh fennel bulb"
print parse(text)







#outfile = open("./epicurious-chowders.csv", "wb")
#writer = csv.writer(outfile)
#writer.writerows(recipe_array)