
"""
Code Challenge

https://en.wikipedia.org/wiki/List_of_states_and_union_territories_of_India_by_area


Scrap the data from State/Territory and National Share (%) columns for top 6 
states basis on National Share (%). 
Create a Pie Chart using MatPlotLib and explode the state with largest national share %.

"""

import requests
from bs4 import BeautifulSoup 
import matplotlib.pyplot as plt

url = "https://en.wikipedia.org/wiki/List_of_states_and_union_territories_of_India_by_area"
data = requests.get(url).text
soup = BeautifulSoup(data, "lxml")

all_table= soup.find_all('table')

right_table= soup.find('table', class_= 'wikitable')

A = []
B = []

for row in right_table.findAll('tr'):
    cells = row.findAll('td')

    if len(cells) == 7:
        A.append(cells[1].text.strip())
        B.append(cells[4].text.strip())

labels = (A[0],A[1],A[2],A[3],A[4],A[5])
sizes = B[0:6]
explode = [0.1,0,0,0,0,0]
colors = ['blue', 'orange','gold', 'yellowgreen', 'lightcoral', 'lightskyblue']

plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.savefig('National_share.jpg')



"""
Code Challenge 

import Automobile.csv file.

Using MatPlotLib create a PIE Chart of top 10 car makers according to the number 
of their cars and explode the largest car maker


"""
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("Automobile.csv")
series=df['make'].value_counts().head(10)
explode=[.2,0,0,0,0,0,0,0,0,0]
plt.pie(series.values,explode,series.index,autopct='%2.2f%%')

"""
Code Challenge
  Name: 
    SSA Analysis
  Filename: 
    ssa.py
  Problem Statement:
    (Baby_Names.zip)
    The United States Social Security Administration (SSA) has made available 
    data on the frequency of baby names from 1880 through the 2010. 
    (Use Baby_Names.zip from Resources)  
    
    Read data from all the year files starting from 1880 to 2010, 
    add an extra column named as year that contains year of that particular data
    Concatinate all the data to form single dataframe using pandas concat method
    Display the top 5 male and female baby names of 2010
    Calculate sum of the births column by sex as the total number of births 
    in that year(use pandas pivot_table method)
    Plot the results of the above activity to show total births by sex and year  
     

import pandas as pd
import os
count=0
df=pd.DataFrame()
for file in os.listdir():
    if file.endswith('.txt') and count<=130:
        with open(file ,mode='rt') as file1:
            data=file1.read().split()
        year=file[3:7]
        df[year]=pd.Series(data)
        count=count+1
"""

import pandas as pd

df1=pd.DataFrame(['Name', 'Sex', 'Number','Year'])
for i in range(1880,2018):
    filename="yob"+str(i)+".txt"
    df2 = pd.read_csv(filename,header=None)
    df2.columns = ['Name', 'Sex', 'Number']
    df2['Year']=i
    df2 = df2.sort_values(by=['Number'], ascending=False)
    df1=pd.concat([df1, df2])   
print("Top 5 male baby name in 2017\n",df1[(df1["Sex"] == "M") & (df1["Year"] == 2010)].head(5))
print("Top 5 male baby name in 2017\n",df1[(df1["Sex"] == "F") & (df1["Year"] == 2010)].head(5))

df=df1.groupby(['Year', 'Sex'])['Number'].aggregate('sum').unstack()
df.plot()


"""
Code Challenge
  Name: 
    URL shortening service Bitly
  Filename: 
    bitly.py
  Problem Statement:
    (usagov_bitly_data.json)
    In 2011, URL shortening service Bitly partnered with the US government website
    USA.gov to provide a feed of anonymous data gathered from users who shorten links
    ending with .gov or .mil. 
    In 2011, a live feed as well as hourly snapshots were available
    as downloadable text files. 
    This service is shut down at the time of this writing (2017),
    but we preserved one of the data files.
    In the case of the hourly snapshots, each line in each file contains a common form of
    web data known as JSON. (Use usagov_bitly_data.txt file from Resources)

    Replace the 'nan' values with 'Mising' and ' ' values with 'Unknown' keywords
    Print top 10 most frequent time-zones from the Dataset i.e. 'tz', with and without Pandas
    Count the number of occurrence for each time-zone
    Plot a bar Graph to show the frequency of top 10 time-zones (using Seaborn)
    From field 'a' which contains browser information and separate out browser capability(i.e. the first token in the string eg. Mozilla/5.0)
    Count the number of occurrence for separated browser capability field and plot bar graph for top 5 values (using Seaborn)
    Add a new Column as 'os' in the dataset, separate users by 'Windows' for the values in  browser information column i.e. 'a' that contains "Windows" and "Not Windows" for those who don't

Hint:
    http://1usagov.measuredvoice.com/2011/
    
"""

import pandas as pd
import numpy as np
from collections import Counter
json_df = pd.read_json("usagov_bitly_data.json", lines=True)
    # Repalcing some data with some other data
json_df = json_df.replace([np.nan, ""], ["Mising", "Unknown"])
    # Getting the top 10 timezones frequency using pandas method
json_df_timezone = json_df['tz'].value_counts().head(10)
    # Getting frequency of each timezones
tz_count = json_df['tz'].value_counts()
    # To draw the top 10 timezones frequnecy bar graph for a series we can use Series.plot.type()
json_df_timezone.plot.bar()

tokens_df = json_df['a'].str.split(n=1, expand=True)
    # Fetching the frequency of the browser capability
token_freq = tokens_df['Token_0'].value_counts()
    # Plotting bar graph for top 5 browser capability
token_freq.head().plot.bar()
tokens_df=tokens_df.replace(np.nan,"Mising")
tokens_df["os"] = 'Not Windows'
i=0
while i<576:
    a=tokens_df[1][i]
    if a.find("Windows")==1:
        tokens_df["os"][i]="Windows"
    i=i+1


"""
Code Challenge
  Name: 
    Baltimore City Analysis
  Filename: 
    baltimore.py
  Problem Statement:
    Read the Baltimore_City_Employee_Salaries_FY2014.csv file 
    and perform the following task :

    0. remove the dollar signs in the AnnualSalary field and assign it as a float
    0. Group the data on JobTitle and AnnualSalary, and aggregate with sum, mean, etc.
       Sort the data and display to show who get the highest salary
    0. Try to group on JobTitle only and sort the data and display
    0. How many employess are there for each JobRoles and Graph it
    0. Graph and show which Job Title spends the most
    0. List All the Agency ID and Agency Name 
    0. Find all the missing Gross data in the dataset 
    
  Hint:

import pandas as pd
import requests
import StringIO as StringIO
import numpy as np
        
url = "https://data.baltimorecity.gov/api/views/2j28-xzd7/rows.csv?accessType=DOWNLOAD"
r = requests.get(url)
data = StringIO.StringIO(r.content)

dataframe = pd.read_csv(data,header=0)

dataframe['AnnualSalary'] = dataframe['AnnualSalary'].str.lstrip('$')
dataframe['AnnualSalary'] = dataframe['AnnualSalary'].astype(float)

# group the data
grouped = dataframe.groupby(['JobTitle'])['AnnualSalary']
aggregated = grouped.agg([np.sum, np.mean, np.std, np.size, np.min, np.max])

# sort the data
pd.set_option('display.max_rows', 10000000)
output = aggregated.sort(['amax'],ascending=0)
output.head(15)


aggregated = grouped.agg([np.sum])
output = aggregated.sort(['sum'],ascending=0)
output = output.head(15)
output.rename(columns={'sum': 'Salary'}, inplace=True)


from matplotlib.ticker import FormatStrFormatter

myplot = output.plot(kind='bar',title='Baltimore Total Annual Salary by Job Title - 2014')
myplot.set_ylabel('$')
myplot.yaxis.set_major_formatter(FormatStrFormatter('%d'))

"""

import pandas as pd
import numpy as np
df = pd.read_csv('Baltimore_City_Employee_Salaries_FY2014.csv',header=0)
df['AnnualSalary'] = df['AnnualSalary'].astype(str)
df['AnnualSalary'].apply(lambda x: x.replace('$',''))
df['AnnualSalary'] = df['AnnualSalary'].astype(float)
# group the data
group_jt_as = df.groupby(['JobTitle'])['AnnualSalary']
aggregated = group_jt_as.agg([np.sum, np.mean, np.std, np.size, np.min, np.max])
annual_salary = df.sort_values(['AnnualSalary'],ascending=0)
print (str(annual_salary.iloc[0,0])+" get the highest salary")

#grouped = df.groupby(['JobTitle'])
#sorted(grouped.keys())

# Top 10 jobroles according to employees numbers
df['JobTitle'].value_counts()[0:10].plot('bar')

#  which Job Title spends the most
aggregated.sort_values(['sum'],ascending=0,inplace=True)
print (str(aggregated.index[0])+" job title spends the most")

aggregated['sum'][0:10].plot('bar')

# List All the Agency ID and Agency Name
agency_name_id = df[['Agency','AgencyID']]
agency_name_id.drop_duplicates(inplace=True)
print(agency_name_id)
# Find all the missing Gross data in the dataset
df['GrossPay'].isnull().sum()

"""
Code Challenge
  Name: 
    IGN Analysis
  Filename: 
    ign.py
  Problem Statement:
    Read the ign.csv file and perform the following task :
   
   Let's say we want to find games released for the Xbox One 
   that have a score of more than 7.
   
   review distribution for the Xbox One vs the review distribution 
   for the PlayStation 4.We can do this via a histogram, which will plot the 
   frequencies for different score ranges.
   
   
   
  Hint:

    The columns contain information about that game:

    score_phrase — how IGN described the game in one word. 
                   This is linked to the score it received.
    title — the name of the game.
    url — the URL where you can see the full review.
    platform — the platform the game was reviewed on (PC, PS4, etc).
    score — the score for the game, from 1.0 to 10.0.
    genre — the genre of the game.
    editors_choice — N if the game wasn't an editor's choice, Y if it was. This is tied to score.
    release_year — the year the game was released.
    release_month — the month the game was released.
    release_day — the day the game was released.



xbox_one_filter = (reviews["score"] > 7) & (reviews["platform"] == "Xbox One")
filtered_reviews = reviews[xbox_one_filter]
filtered_reviews.head()
      
%matplotlib inline
reviews[reviews["platform"] == "Xbox One"]["score"].plot(kind="hist")

reviews[reviews["platform"] == "PlayStation 4"]["score"].plot(kind="hist")

filtered_reviews["score"].hist()
        
"""

import pandas as pd
df = pd.read_csv('ign.csv')
# games released for the Xbox One that have a score of more than 7
xbox_one_filter = (df["score"] > 7) & (df["platform"] == "Xbox One")
filtered_reviews = df[xbox_one_filter]
games_xbox_one= filtered_reviews['title']
print (games_xbox_one)

# review distribution for the Xbox One
xbox_one =(df['platform']=="Xbox One")
xbox_one_only = df[xbox_one]
xbox_one_reviews = xbox_one_only['score_phrase']
xbox_one_reviews.hist(bins=20,grid=False,xrot=90)

# review distribution for the PlayStation 4
ps4 = df['platform']=="PlayStation 4"
ps4_only_df = df[ps4]
ps4_reviews = ps4_only_df['score_phrase']
ps4_reviews.hist(bins=20,grid=False,xrot=90)



