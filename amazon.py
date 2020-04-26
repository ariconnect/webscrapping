from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup
import smtplib
import time

URL = "https://www.amazon.de/Sony-Alpha-Digitalkamera-Set-spiegellos-Schwarz/dp/B0721N16PK/ref=sr_1_5?__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=3AB7DOQ8TYV1O&dchild=1&keywords=sony+digitalkamera&qid=1587893796&sprefix=sony+digita%2Caps%2C266&sr=8-5"

uClient = uReq(URL)
page_html  = uClient.read()
uClient.close()
# print(soup.prettify())


def check_price():
    soup = BeautifulSoup(page_html,"html.parser")
    title = soup.find("h1")
    product_name = title.text
    print(product_name.strip())

    sub_title = soup.find("td",{"class":"a-span12"})
    price = sub_title.text.strip()
    converted_price=price[0:5]
    final_price = float(converted_price.replace(".", ""))
    print(final_price)

    if final_price < 1100:
        send_mail()

def send_mail():
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login("arinze@estendo.net","anyaeche1")

    subject = "Low price"
    body = "Check the Amazon link- https://www.amazon.de/Sony-Alpha-Digitalkamera-Set-spiegellos-Schwarz/dp/B0721N16PK/ref=sr_1_5?__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=3AB7DOQ8TYV1O&dchild=1&keywords=sony+digitalkamera&qid=1587893796&sprefix=sony+digita%2Caps%2C266&sr=8-5"
    msg ="Subject: {}\n\n{}".format(subject,body)
    server.sendmail("arinze@estendo.net",
        "arinze.anyaeche@gmail.com",msg)

    print("Email has been sent :)")
    server.quit()


while True:
    check_price()
    time.sleep(60*60) #run and delay the execution for 60 seconds
