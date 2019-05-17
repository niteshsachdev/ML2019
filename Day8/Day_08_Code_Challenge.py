"""
Code Challenge
  Name: 
    Webscrapping ICC Cricket Page
  Filename: 
    icccricket.py
  Problem Statement:
    Write a Python code to Scrap data from ICC Ranking's 
    page and get the ranking table for ODI's (Men). 
    Create a DataFrame using pandas to store the information.
  Hint: 
    https://www.icc-cricket.com/rankings/mens/team-rankings/odi 
    
    
    #https://www.icc-cricket.com/rankings/mens/team-rankings/t20i
    #https://www.icc-cricket.com/rankings/mens/team-rankings/test
"""


from bs4 import BeautifulSoup
import requests
odi = "https://www.icc-cricket.com/rankings/mens/team-rankings/odi"
source = requests.get(odi).text
soup = BeautifulSoup(source,"lxml")
right_table=soup.find('table', class_='table')
print (right_table)
A=[]
B=[]
C=[]
D=[]
E=[]
for row in right_table.findAll('tr'):
    cells=row.findAll('td')
    if(len(cells)==5):
        A.append(cells[0].text.strip())
        B.append(cells[1].text.strip())
        C.append(cells[2].text.strip())
        D.append(cells[3].text.strip())
        E.append(cells[4].text.strip())

import pandas as pd
from collections import OrderedDict

col_name = ["Pos","Team","Weighted Matches","Points","Rating"]
col_data = OrderedDict(zip(col_name,[A,B,C,D,E]))
df = pd.DataFrame(col_data) 
df.to_csv("former.csv")
     

"""
Code Challenge:
  Name: 
    Bid Plus
  Filename: 
    bid_plus.py
  Problem Statement:
      USE SELENIUM
      Write a Python code to Scrap data and download data from given url.
      url = "https://bidplus.gem.gov.in/bidlists"
      Make list and append given data:
          1. BID NO
          2. items
          3. Quantity Required
          4. Department Name And Address
          5. Start Date/Time(Enter date and time in different columns)
          6. End Date/Time(Enter date and time in different columns)
     Make a csv file add all data in it.
      csv Name: bid_plus.csv
"""
     
from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup
url = "https://bidplus.gem.gov.in/bidlists"
browser = webdriver.Chrome("C:/Users/Nitesh Sachdev/Desktop/Forsk ML/Day8/chromedriver.exe")
browser.get(url)
sleep(2)
item=[]
quantity=[]
dept=[]
start_date=[]
end_date=[]
for i in range(1,11):
    data_bid_no = browser.find_element_by_xpath('//*[@id="pagi_content"]/div[1]/div[1]/p[1]/a')
    data_bid_no.click()
    sleep(2)
    item.append(browser.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[2]/p[1]/span').text)
    quantity.append(browser.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[2]/p[2]/span').text)
    dept.append(browser.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[3]/p[2]').text)
    start_date.append(browser.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[4]/p[1]/span').text)
    end_date.append(browser.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[4]/p[2]/span').text)
import pandas as pd
from collections import OrderedDict

col_name = ["Items","Quantity Required","Department Name and Address","Start Date","End Date"]
col_data = OrderedDict(zip(col_name,[item,quantity,dept,start_date,end_date]))
df = pd.DataFrame(col_data) 
df.to_csv("former.csv")




"""
http://forsk.in/images/Forsk_logo_bw.png"

Download the image from the url above and store in your workking diretory with the same
name as the image name.

Do not hardcode the name of the image

"""


from PIL import Image
from bs4 import BeautifulSoup
from io import BytesIO
import requests
url= "http://forsk.in/images/Forsk_logo_bw.png"
img=requests.get(url)
a=Image.open(BytesIO(img.content))
img_content=BeautifulSoup(url,"lxml")
name=img_content.text.split("/")[-1]
a.save(name)