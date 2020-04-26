import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = "https://www.jumia.com.ng/firman-generator-spg1800-1.1kva-sumec-mpg53324.html"

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                         "Chrome/80.0.3987.163 Safari/537.36"}

page = requests.get(URL, headers=headers)

def check_price():
    soup = BeautifulSoup(page.content,"html.parser")
    title = soup.findAll("h1")
    product_name= soup.h1.get_text()
    print(product_name)

    sub_title = soup.findAll("span",{"class":"-b -ltr -tal -fs24"})
    price = sub_title[0].text
    converted_price = price[1:].strip()
    final_price = float(converted_price.replace(",", ""))
    print(final_price)

    if final_price < 63000:
        send_mail()

def send_mail():
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login("arinze@estendo.net","anyaeche1")

    subject = "Low price"
    body = "Check the Jumia link- https://www.jumia.com.ng/firman-generator-spg1800-1.1kva-sumec-mpg53324.html"
    msg ="Subject: {}\n\n{}".format(subject,body)
    server.sendmail("arinze@estendo.net",
        "arinze.anyaeche@gmail.com",msg)

    print("Email has been sent :)")
    server.quit()
time_delay = (60*60*24)
print(time_delay)
while True:
    check_price()
    time.sleep(time_delay) #run and delay the execution for 60 seconds
