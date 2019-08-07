"""
Code Challenge:
dataset: BreadBasket_DMS.csv

Q1. In this code challenge, you are given a dataset which has data and time wise transaction on a bakery retail store.
1. Draw the pie chart of top 15 selling items.
2. Find the associations of items where min support should be 0.0025, min_confidence=0.2, min_lift=3.
3. Out of given results sets, show only names of the associated item from given result row wise.
"""
import pandas as pd
from apyori import apriori
import matplotlib.pyplot as plt 
dataset=pd.read_csv("BreadBasket_DMS.csv")
#1. Draw the pie chart of top 15 selling items.
top_items=dataset['Item'].value_counts()
plt.pie(top_items.values[:15],labels=top_items.index[0:15],autopct='%0.2f%%')

#2. Find the associations of items where min support should be 0.0025, min_confidence=0.2, min_lift=3.
dataset=dataset.mask(dataset.eq('NONE')).dropna()

def transation(values):
    str1=",".join(values)
    return str1.split(',')
df=dataset.groupby('Transaction')["Item"].apply(transation)


rules = apriori(df, min_support = 0.0025, min_confidence = 0.2, min_lift = 3)

# Visualising the results
results = list(rules)

for item in results:

    # first index of the inner list
    # Contains base item and add item
    pair = item[0] 
    items = [x for x in pair]
    print("Rule: " + items[0] + " -> " + items[1])

    #second index of the inner list
    print("Support: " + str(item[1]))

    #third index of the list located at 0th
    #of the third index of the inner list

    print("Confidence: " + str(item[2][0][2]))
    print("Lift: " + str(item[2][0][3]))
    print("=====================================")

#3. Out of given results sets, show only names of the associated item from given result row wise.
for item in results:
    pair = item[0] 
    items = [x for x in pair]
    print("Rule: " + items[0] + " -> " + items[1])


"""
Code Challenge:
Datset: Market_Basket_Optimization.csv
Q2. In today's demo sesssion, we did not handle the null values before fitting the data to model, remove the null values from each row and perform the associations once again.
Also draw the bar chart of top 10 edibles.
"""

# Importing the libraries
import pandas as pd
from apyori import apriori

# Data Preprocessing
dataset = pd.read_csv('Market_Basket_Optimisation.csv', header = None)



transactions = []
tran=[]
for i in range(0, 7501):
    #transactions.append(str(dataset.iloc[i,:].values)) #need to check this one
    tran=[]
    for j in range(0, 20):
        if str(dataset.iloc[i,:][j])!='nan':
            tran.append(str(dataset.values[i,j]))
    transactions.append(tran)    
# Training Apriori on the dataset

rules = apriori(transactions, min_support = 0.003, min_confidence = 0.25, min_lift = 4)

# Visualising the results
results = list(rules)




for item in results:

    # first index of the inner list
    # Contains base item and add item
    pair = item[0] 
    items = [x for x in pair]
    print("Rule: " + items[0] + " -> " + items[1])

    #second index of the inner list
    print("Support: " + str(item[1]))

    #third index of the list located at 0th
    #of the third index of the inner list

    print("Confidence: " + str(item[2][0][2]))
    print("Lift: " + str(item[2][0][3]))
    print("=====================================")
# top 10 edibles
edibles=[]
for i in range(0, 7501):
    for j in range(0, 20):
        if str(dataset.iloc[i,:][j])!='nan':
            edibles.append(str(dataset.values[i,j]))
data=pd.DataFrame(edibles)
top_edibles=data[0].value_counts()

df=pd.DataFrame({'edibles':list(top_edibles.index[0:10]),'count':list(top_edibles.values[0:10])})
ax=df.plot.bar(x='edibles',y='count',rot=90)
