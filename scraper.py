import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = 'https://www.amazon.de/Sony-Systemkamera-Megapixel-LCD-Display-SEL-P1650/dp/B00IE9XHE0/ref=sr_1_1?crid' \
      '=O6WNORIW6HVH&keywords=sony+alpha+6000&qid=1569265230&s=gateway&sprefix=sony+a%2Caps%2C131&sr=8-1 '

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/76.0.3809.132 Safari/537.36'}

def check_price():
    page = requests.get(URL, headers=headers)


    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="productTitle").get_text() #Gets title of product
    price = soup.find(id="priceblock_ourprice").get_text() #Gets price of product
    converted_price = float(price[0:3]) #Converts price to float to allow comparison

    if(converted_price < 500): #Compare price
        send_mail()

    print(converted_price)
    print(title.strip())

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('yacer.tirsen@gmail.com', 'XXXXXXXXX') #Email Log in credentials 

    subject = 'Price dropped for Amazon product!'
    body = 'Check the Amazon link https://www.amazon.de/Sony-Systemkamera-Megapixel-LCD-Display-SEL-P1650/dp/B00IE9XHE0/ref=sr_1_1?crid' \
      '=O6WNORIW6HVH&keywords=sony+alpha+6000&qid=1569265230&s=gateway&sprefix=sony+a%2Caps%2C131&sr=8-1'

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'yacer.tirsen@gmail.com',
        'mordants@yahoo.com',
        msg
    )

    print("Email has been sent!")

    server.quit()

while(True):
    check_price()
    time.sleep(86400) #Checks on the price every 24hrs


