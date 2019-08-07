"""

Code Challenge
  Name: 
    Student and Faculty JSON
  Filename: 
    student.json
    faculty.json
  Problem Statement:
    Create a student and Faculty JSON object and get it verified using jsonlint.com
    Write a JSON for faculty profile. 
    The JSON should have profile of minimum 2 faculty members. 
    The profile for each faculty should include below information atleast:

        First Name
        Last Name
        Photo (Just a random url)
        Department 
        Research Areas (can be multiple)
        Contact Details (should include phone number and email id and can have multiple )
   Hint:
       www.jsonlint.com
       
"""
json_student_factulty="""{
	"faculty": [{
			"Fname": "abc",
			"lname": "xyz",
			"photo": "C:/Users/Nitesh Sachdev/Desktop/Forsk ML/Day7",
			"department": "cs",
			"research_area": ["ML", "AI"],
			"contact_details": 954321354
		},
		{
			"Fname": "abc",
			"lname": "xyz",
			"photo": "C:/Users/Nitesh Sachdev/Desktop/Forsk ML/Day7",
			"department": "cs",
			"research_area": ["ML", "AI"],
			"contact_details": 954321354
		}
	],
	"students": [{
			"Fname": "abc",
			"lname": "xyz",
			"photo": "C:/Users/Nitesh Sachdev/Desktop/Forsk ML/Day7",
			"department": "cs",
			"research_area": ["ML", "AI"],
			"contact_details": 954321354
		},
		{
			"Fname": "abc",
			"lname": "xyz",
			"photo": "C:/Users/Nitesh Sachdev/Desktop/Forsk ML/Day7",
			"department": "cs",
			"research_area": ["ML", "AI"],
			"contact_details": 954321354
		}
	]
}
"""


"""
Code Challenge
  Name: 
    JSON Parser
  Filename: 
    json.py
  Problem Statement:
    Get me the other details about the city
        Latitude and Longitude
        Weather Condition
        Wind Speed
        Sunset Rise and Set timing
"""

import requests
import time
url1 = "http://api.openweathermap.org/data/2.5/weather"
url2 = "?q=Jaipur"
url3 = "&appid=e9185b28e9969fb7a300801eb026de9c"
url=url1+url2+url3
print(url)
response=requests.get(url)
#print(response.content)
jsondata = response.json()
#new_json_string = json.dumps(jsondata, indent=2 )
#print (new_json_string) 
print("Latitude {} and Longitude {}".format(jsondata["coord"]["lon"],jsondata["coord"]["lat"]))
print("Weather Condition - {}".format(jsondata["weather"][0]["main"]))
print("Wind speed : {}".format(jsondata["wind"]["speed"]))
sunrise=time.strftime("%H:%M:%S",time.gmtime(jsondata["sys"]["sunrise"]))
sunset=time.strftime("%H:%M:%S",time.gmtime(jsondata["sys"]["sunset"]))
print("Sunset Rise: {} and set timing: {}".format(sunrise,sunset))



"""
Code Challenge
  Name: 
    Currency Converter Convert  from USD to INR
  Filename: 
    currecncyconv.py
  Problem Statement:
    You need to fetch the current conversion prices from the JSON  
    using REST API
  Hint:
    http://free.currencyconverterapi.com/api/v5/convert?q=USD_INR&compact=y
    Check with http://api.fixer.io/latest?base=USD&symbol=EUR
    
"""
import requests
num=input("Enter the USD amount")
url1="http://data.fixer.io/api/latest"
url2="?access_key=ecbb32a41bfb25c3ebe52b8542210610"
url3="& symbols = USD"
url=url1+url2+url3
response=requests.get(url)
jsondata = response.json()
print("USD to INR of {} is {}".format(float(num),float(num)*(jsondata["rates"]["INR"])))
# Create a new Code Challenge to POST data 

# Research the below wesbite and post some data on it

# https://requestbin.com



import json
import requests
Host = "http://13.127.155.43/api_v0.1/sending"
data = {"Phone_Number":9549306166,"Name":"Nitesh Sachdev","College_Name":"PIET","Branch":"CS"}
headers = {"Content-Type":"application/json","Content-Length":len(data),"data":json.dumps(data)}
def post_method():
    response = requests.post(Host,data,headers)
    return response
print ( post_method().text )
def get_method():
    response = requests.get("http://13.127.155.43/api_v0.1/receiving")
    return response

print (get_method().text)
