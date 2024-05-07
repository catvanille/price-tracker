import requests
from bs4 import BeautifulSoup
from frontend.get import *
import smtplib
URL = 'https://jolse.com/product/beauty-of-joseon-relief-sun-rice-probiotics-50ml/46958/category/1/display/22/'

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"}

def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find('meta', attrs={'property': 'recopick:title'})
    og_price = soup.find('meta', attrs={'property': 'recopick:price'})
    sale_price = soup.find('meta', attrs={'property': 'recopick:sale_price'})
    convert_og_price = float(og_price['content'])
    convert_sale_price = float(sale_price['content'])

    percent_off = (convert_og_price - convert_sale_price) / convert_og_price * 100
    if input_percent >= percent_off:
        send_mail()
        
def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('

