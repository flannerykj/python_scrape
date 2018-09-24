
import csv
import requests
import socket
from bs4 import BeautifulSoup

#https://en.wikipedia.org/wiki/List_of_postal_codes_of_Canada:_A

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def get_codes_for_letter(letter):
    codes = []
    try:
        url = 'https://en.wikipedia.org/wiki/List_of_postal_codes_of_Canada:_%s' % letter
        response = requests.get(url)
        html = response.content
        soup = BeautifulSoup(html, features="html.parser")
        cell_list = soup.findAll('td')
        for item in cell_list:
            codeNode = item.find('b')
            if codeNode:
                assigned = item.find('a')
                unassigned = item.find('i')
                if assigned:
                    if len(codeNode.text) < 4:
                        codes.append(codeNode.text)

        return codes
    except Exception as e:
        print (e.message)
        return codes

all_codes = []

i = 0
while i < len(alphabet):
    result = get_codes_for_letter(alphabet[i])
    print(result)
    if len(result) > 0:
        all_codes.append(result)
    i += 1

with open("./postal_codes.csv",'w') as resultFile:
    wr = csv.writer(resultFile, dialect='excel')
    for letter_codes in all_codes:
        wr.writerow(letter_codes)
