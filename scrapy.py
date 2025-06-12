import requests
from bs4 import BeautifulSoup

def get_scrapy(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    precious = []
    for price in soup.find_all('span', class_="andes-money-amount__fraction", ):
        value = price.string
        precious.append(value)
    return precious
   

ml_url = "https://lista.mercadolivre.com.br/ssd#D[A:ssd]"

products = get_scrapy(ml_url)
for product in sorted(products):
    print("R$",product)