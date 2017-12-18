
import csv
import requests
import socket
from bs4 import BeautifulSoup
import re
import json

def parse_artists():
    artist_profiles = []
    try:
        url = 'http://wx.toronto.ca/inter/pmmd/streetart.nsf/artists?OpenView'
        response = requests.get(url)
        html = response.content
        soup = BeautifulSoup(html)
        link_list = soup.findAll('a', attrs={'class': 'viewa1'})
        for item in link_list:
            item_url = 'http://wx.toronto.ca'+item.get('href')
            profile = get_profile_data(item_url)
            artist_profiles.append(profile)
    except Exception as e:
        print (e.message)
    return artist_profiles

def get_profile_data(url):
    try:
        response = requests.get(url)
        html = response.content
        soup = BeautifulSoup(html)
        profile = soup.find('div', attrs={'id': 'profiledisplay'}).text
        name = soup.findAll('legend')[0].text
        email = re.search(r'[\w\.-]+@[\w\.-]+', profile).group().replace('Business', '')
        website = re.search(r'Website: (.*?)[\n\r\s]+', profile).group().replace('Website: ', '')
        bio = re.search(r'Profile\n(.*?)\n', profile).group().replace('Profile', '')
        description = re.search(r'Business/Organization Description\n(.*?)\n', profile).group().replace('Business/Organization Description', '')
        experience = re.search(r'Experience\n(.*?)\n', profile).group().replace('Experience', '')
        return {
            "name": name,
            "email": email,
            "website": website,
            "bio": bio,
            "description": description,
            "experience": experience,
            "dateJoined": "1508884475917",
            "dateUpdated": "1508884475917"
            }

        return profile
    except Exception as e:
        print (e.message)
    return

with open('artists.json', 'w') as outfile:
    json.dump(parse_artists(), outfile)

'''artist_urls = get_artist_urls()
artist_array = compile_artist_profiles(artist_urls)

outfile = open("./toronto-artists.csv", "wb")
writer = csv.writer(outfile)
writer.writerows(recipe_array)'''

