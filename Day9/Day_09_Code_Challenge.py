 
"""

Code Challenge 1
Write a python code to insert records to a mongo/sqlite/MySQL database 
named db_University for 10 students with fields like 
Student_Name, Student_Age, Student_Roll_no, Student_Branch.
"""

import pymongo
client = pymongo.MongoClient("mongodb://niteshsachdev:tUFBfkAC0GlUHJ6U@cluster0-shard-00-00-6ilnm.mongodb.net:27017,cluster0-shard-00-01-6ilnm.mongodb.net:27017,cluster0-shard-00-02-6ilnm.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true")

mydb = client.db_University
def add_student(student_name, student_age, student_roll_no, student_branch):
    mydb.student_db.insert_one(
            {
            "student_name" : student_name,
            "student_age" : student_age,
            "student_roll_no" : student_roll_no,
            "student_branch" : student_branch
            })
    return "Employee added successfully"
def fetch_all_student():
    user = mydb.student_db.find()
    for i in user:
        print (i)


add_student('Sylvester',25,1,'CS')
add_student('Yogendra', 25,2,'CS')
add_student('Rohit', 25,3,'CS')
add_student('Kunal', 25,4,'CS')
add_student('Devendra', 25,5,'CS')

fetch_all_student()
#---------------------------using mysql

import mysql.connector 
conn = mysql.connector.connect(user='niteshsachdev', password='niteshsachdev',host='db4free.net', database = 'db_college')
c = conn.cursor()
c.execute ("""CREATE TABLE student(
          student_name TEXT,
          student_age INTEGER,
          student_roll_no INTEGER,
          student_branch TEXT
          )""")
c.execute("INSERT INTO student VALUES ('Sylvester',25,1,'CS')")
c.execute("INSERT INTO student VALUES ('Yogendra', 25,2,'CS')")
c.execute("INSERT INTO student VALUES ('Rohit', 25,3,'CS')")
c.execute("INSERT INTO student VALUES ('Kunal', 25,4,'CS')")
c.execute("INSERT INTO student VALUES ('Devendra', 25,5,'CS')")
c.execute("SELECT * FROM student")
print ( c.fetchall() )
conn.commit()
conn.close()

#------------------------using sqlite


import sqlite3
conn = sqlite3.connect ( 'student.db' )
c = conn.cursor()
c.execute ("""CREATE TABLE student(
          student_name TEXT,
          student_age INTEGER,
          student_roll_no INTEGER,
          student_branch TEXT
          )""")
c.execute("INSERT INTO student VALUES ('Sylvester',25,1,'CS')")
c.execute("INSERT INTO student VALUES ('Yogendra', 25,2,'CS')")
c.execute("INSERT INTO student VALUES ('Rohit', 25,3,'CS')")
c.execute("INSERT INTO student VALUES ('Kunal', 25,4,'CS')")
c.execute("INSERT INTO student VALUES ('Devendra', 25,5,'CS')")
c.execute("SELECT * FROM student")
print ( c.fetchall() )
conn.commit()
conn.close()


"""
Code Challenge 2
Perform similar steps as in the above code challenge but store the contents in 
an online mongo atlas database.
"""

import pymongo
client = pymongo.MongoClient("mongodb://niteshsachdev:tUFBfkAC0GlUHJ6U@cluster0-shard-00-00-6ilnm.mongodb.net:27017,cluster0-shard-00-01-6ilnm.mongodb.net:27017,cluster0-shard-00-02-6ilnm.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true")

mydb = client.db_University
def add_student(student_name, student_age, student_roll_no, student_branch):
    mydb.student_db.insert_one(
            {
            "student_name" : student_name,
            "student_age" : student_age,
            "student_roll_no" : student_roll_no,
            "student_branch" : student_branch
            })
    return "Employee added successfully"
def fetch_all_student():
    user = mydb.student_db.find()
    for i in user:
        print (i)


add_student('Sylvester',25,1,'CS')
add_student('Yogendra', 25,2,'CS')
add_student('Rohit', 25,3,'CS')
add_student('Kunal', 25,4,'CS')
add_student('Devendra', 25,5,'CS')

fetch_all_student()


"""
Code Challenge 3
In the Bid plus Code Challenege 

          1. BID NO
          2. items
          3. Quantity Required
          4. Department Name And Address
          5. Start Date/Time(Enter date and time in different columns)
          6. End Date/Time(Enter date and time in different columns)

Store the information into a database mySQL Database
"""

from selenium import webdriver
from time import sleep
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

import mysql.connector 
conn = mysql.connector.connect(user='bidniteshsachdev', password='bidniteshsachdev',host='db4free.net', database = 'bid_database')
c = conn.cursor()
c.execute ("""CREATE TABLE bid(
          items TEXT,
          quantity INTEGER,
          department TEXT,
          start_date TEXT,
          end_date TEXT
          )""")
for i in range(1,11):
    c.execute("INSERT INTO bid VALUES ('"+item[i]+"',"+quantity[i]+",'"+dept[i]+"','"+start_date[i]+"','"+end_date[i]+"')")
c.execute("SELECT * FROM bid")
print ( c.fetchall() )
conn.commit()
conn.close()



"""
Code Challenge 4

Scrap the data from the URL below and store in sqlite database

https://www.icc-cricket.com/rankings/mens/team-rankings/odi
"""



import sqlite3
conn = sqlite3.connect ( 'men_odi.db' )
c = conn.cursor()
c.execute ("""CREATE TABLE odi(
          pos TEXT,
          team TEXT,
          weighter_matches TEXT,
          points TEXT,
          rating TEXT
          )""")
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
for i in range(len(A)):
    c.execute("INSERT INTO odi VALUES ('"+A[i]+"','"+B[i]+"','"+C[i]+"','"+D[i]+"','"+E[i]+"')")
c.execute("SELECT * FROM odi")
print ( c.fetchall() )
conn.commit()
conn.close()
     





































def make_number_prime(num):
  for i in str(num):
    new.append(i)
  new1=sorted(new,reverse=True)
  new_num="".join(new1)
  print(new_num)
"""
  for i in range(1,num):
    if num%i==0:
      list1.append(i)
  if len(list1)==0:
    print("-1")
  else:
    print(max(list1))

"""
new=[]
list1=[]
num = int(input())
print(make_number_prime(num))










no_of_dolls = input()
dolls_id = input().strip(" ").split(",")
dolls_height = list(map(int, input().strip(" ").split(",")))
new_id=dolls_id
new_height=dolls_height
new_height1=sorted(new_height)
swap=''
for i in range(len(new_height1)):
    for j in range(len(dolls_height)):
        if (new_height1[i]==dolls_height[j]):
            swap=dolls_id[i]
            dolls_id[i]=dolls_id[j]
            dolls_id[j]=swap
             
print(int(dolls_id[::-1]))  
",".join(dolls_id[::-1])




no_of_dolls = input()
dolls_id = input().strip(" ").split(",")
dolls_height = list(map(int, input().strip(" ").split(",")))



































no_of_dolls = input()
dolls_id = input().strip(" ").split(",")
dolls_height = list(map(int, input().strip(" ").split(",")))
new_height=dolls_height
new_height1=sorted(new_height)
swap=''
for i in range(len(new_height1)):
    for j in range(len(dolls_height)):
        if (new_height1[i]==dolls_height[j]):
            swap=dolls_id[i]
            dolls_id[i]=dolls_id[j]
            dolls_id[j]=swap
dolls_id=",".join(dolls_id[::-1])
dolls_height=new_height1
print(dolls_id)  
