#-*- coding: utf-8 -*

import requests
from bs4 import BeautifulSoup
import smtplib
from time import sleep

link ='https://www.euro.com.pl/grille/tefal-uc600-classic-gc3050.bhtml'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36'}
page = requests.get(link , headers)
soup = BeautifulSoup(page.content, 'html.parser')

title = soup.find(class_="selenium-KP-product-name").get_text().strip()
price = float(soup.find(class_="price-normal").get_text().strip()[0:3])

def check_price():
    if price < 520:
        send_mail()

def send_mail():
    sent_from ='(email)'
    sent_to ='(email)'
    subject = f"CENA SPADlA! {title}"
    text= f"Obnizka ceny! Sprawdz link: {link}"

    msg = f"Subject: {subject}\n\n{text}"

    serwer = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    serwer.ehlo()
    serwer.login('(email)','(pswrd)')
    serwer.sendmail(sent_from, sent_to, msg)
    serwer.ehlo()
    serwer.close()

    print("Wyslano wiadomosc")

check_price()
