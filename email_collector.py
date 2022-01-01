import requests
import bs4
import re

def email_colector():
     url = 'https://www.lifewire.com/best-free-email-accounts-1356641'  # web link from where you want to collect email you can palce your web link here
     text  = requests.get(url)
     data  = bs4.BeautifulSoup(text.text,'html.parser')
     data_string = str(data)

    #strinng = "ankushsoni7171@gmail.com  rahulkuma5000@gmail.com  mzila6482@gmail.com "

    email = re.findall(r"[0-9a-zA-Z._+%]+@[0-9a-zA-Z._+%]+[.][a-zA-Z.0-9]+",data_string)
    print(email)
    return email
email_colector()
