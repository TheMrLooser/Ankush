import requests # for http request
from bs4 import BeautifulSoup # for web scraping
import smtplib # for automated email send
from email.mime.multipart import MIMEMultipart   # for email body
from email.mime.text import MIMEText  # for email body
import datetime  # for taking system date and time
import email_collector # my one file for collecting email from web
now = datetime.datetime.now()

# email content place holder
content = ''

# extracting hacker news

def extract_news(url):
    print("Extracting content from web....")
    cnt =''
    cnt += ('<b> HN TOP STORIES : </b> \n' + '<br>' + '-'*50+'<br>')
    response = requests.get(url)
    content = response.content
    soap = BeautifulSoup(content,'html.parser')
    for i,tag in enumerate(soap.find_all('td',attrs={'class':'title','valign':''})):
        cnt += ((str(i+1)+'::'+tag.text +'\n'+'<br>') if tag.text != 'more' else '')
    return cnt
#
cntnt = extract_news('https://news.ycombinator.com/')
content += cntnt
content += '<br> --------------------- <br>'
content += '<b> Thank, and regard Hacker News </b>'

# sending email
print("Composing email....")

SERVER = 'smtp.gmail.com'  # your smtp server for sending email
PORT = 587 # your port no.
FROM = 'xyz@gmail.com' #  write your email id here

# for getting lists of email
email_list = email_collector.email_colector()
TO  = 'abcd@gmail.com' # clint  email id  on witch you want to send email ,it can be a list
PASS = '********' # write your email password here

msg = MIMEMultipart()
msg['subject'] = 'Top News Stories HN [autometed email]' + '' + str(now.day) +'-'+str(now.month)+'-'+str(now.year)
msg['From'] = FROM
msg['To'] = TO
msg.attach(MIMEText(content,'html'))

print("initializing surver.....")

server = smtplib.SMTP(SERVER,PORT)
server.set_debuglevel(1) # 1 for geting error. 0 for not get error in console if any ocur
server.ehlo()
server.starttls()
server.login(FROM,PASS)
for i in range(len(email_list)):
    TO  = email_list[i]
    print(TO)
    server.sendmail(FROM, TO, msg.as_string())
    i +=1

print("email sent")
server.quit()


# print(TO)








