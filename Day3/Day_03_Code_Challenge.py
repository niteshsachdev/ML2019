
"""
Code Challenge
  Name: 
    generator
  Filename: 
    generator.py
  Problem Statement:
    This program accepts a sequence of comma separated numbers from user 
    and generates a list and tuple with those numbers.  
  Input: 
    2, 4, 7, 8, 9, 12
  Output:
    List : ['2', ' 4', ' 7', ' 8', ' 9', '12'] 
    Tuple : ('2', ' 4', ' 7', ' 8', ' 9', '122')
"""
seq=input("Enter the Sequence")
seq=seq.split(",")
print("List : ",seq)
print("Tuple : ",tuple(seq))

"""
Code Challenge
  Name: 
    weeks
  Filename: 
    weeks.py
  Problem Statement:
    Write a program that adds missing days to existing tuple of days
  Input: 
    ('Monday', 'Wednesday', 'Thursday', 'Saturday')
  Output:
    ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
"""

tuple1=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
list1=input("Enter the days")
list1=list1.split(",")
count=0
print(list1)
for i in tuple1:
    if i not in list1:
        list1.insert(count,tuple1[count])
    count=count+1
print(list1)


"""
Code Challenge
  Name: 
    Supermarket
  Filename: 
    supermarket.py
  Problem Statement:
    You are the manager of a supermarket. 
    You have a list of items together with their prices that consumers bought on a particular day. 
    Your task is to print each item_name and net_price in order of its first occurrence. 
    Take Input from User  
  Hint: 
    item_name = Name of the item. 
    net_price = Quantity of the item sold multiplied by the price of each item.
    try to use new class for dictionary : OrderedDict
  Input:
    BANANA FRIES 12
    POTATO CHIPS 30
    APPLE JUICE 10
    CANDY 5
    APPLE JUICE 10
    CANDY 5
    CANDY 5
    CANDY 5
    POTATO CHIPS 30
  Output:
    BANANA FRIES 12
    POTATO CHIPS 60
    APPLE JUICE 20
    CANDY 20

"""

from collections import OrderedDict
dict1=OrderedDict()
d={}
new_dict={'BANANA FRIES':12,'POTATO CHIPS':30,'APPLE JUICE':10,'CANDY':5}
count=0
while True:
    item_name=input("Enter items and price: ")
    item_name=item_name.split()
    if not item_name:
        break
    last=item_name[-1]
    item_name.remove(last)
    item_name=" ".join(item_name)
    if item_name in d.keys():
        d[item_name]=int(d[item_name])+int(last)
    else:
        d[item_name]=last
print(d)


"""
Code Challenge
  Name: 
    Teen Calculator
  Filename: 
    teen_cal.py
  Problem Statement:
    Take dictionary as input from user with keys, a b c, with some integer 
    values and print their sum. However, if any of the values is a teen -- 
    in the range 13 to 19 inclusive -- then that value counts as 0, except 
    15 and 16 do not count as a teens. Write a separate helper "def 
    fix_teen(n):"that takes in an int value and returns that value fixed for
    the teen rule. In this way, you avoid repeating the teen code 3 times  
  Input: 
    {"a" : 2, "b" : 15, "c" : 13}
  Output:
    Sum = 17
"""

def fix_teen(n):
    if(n in range(13,20)):
        if n == 15 or n==16:
            return n
        return 0
    else:
        return n
d={}
sum1=0
while True:
    name=input("Enter name and age: ")
    name=name.split()
    if not name:
        break
    d[name[0]]=int(name[1])
    sum1=sum1+fix_teen(int(name[1]))
print(d)
print("SUM : ",sum1)

"""
Code Challenge
  Name: 
    Character Frequency
  Filename: 
    frequency.py
  Problem Statement:
    This program accepts a string from User and counts the number of characters (character frequency) in the input string.  
  Input: 
    www.google.com
  Output:
    {'c': 1, 'e': 1, 'g': 2, 'm': 1, 'l': 1, 'o': 3, '.': 2, 'w': 3}
"""

string=input("Enter the string")

dict1={}
for i in string:
    if i in dict1:
        dict1[i]=dict1[i]+1
    else:
        dict1[i]=1
dict1=sorted(dict1.items())
print(dict(dict1))

"""
Code Challenge
  Name: 
    Digit Letter Counter
  Filename: 
    digit_letter_counter.py
  Problem Statement:
    Write a Python program that accepts a string from User and calculate the number of digits and letters.
  Hint:
    Store the letters and Digits as keys in the dictionary  
  Input: 
    Python 3.2
  Output:
    Digits 2
    Letters 6 
"""

string=input("Enter the string")
dict1={'digits':0,'letters':0}
for i in string:
    if i.isalpha():
        dict1['letters']=dict1['letters']+1
    elif i.isdigit():
        dict1['digits']=dict1['digits']+1
print(dict1)


"""
Two words are anagrams if you can rearrange the letters of one to spell the second.  
For example, the following words are anagrams:

 ['abets', 'baste', 'bates', 'beast', 'beats', 'betas', 'tabes']

Hint: How can you tell quickly if two words are anagrams?  
Dictionaries allow you to find a key quickly.  

"""
string1=input("Enter first string ")
string2=input("Enter second string ")
check=0
if len(string)==len(string2):
    for i in string1:
        if i in string2:
            pass
        else:
            check=1
    if check==0:
        print("It is Anagram")
    else:
        print("Not Anagram")
else:
    print("Not Anagram")

"""
Code Challenge
  Name: 
    Intersection
  Filename: 
    Intersection.py
  Problem Statement:
    With two given lists [1,3,6,78,35,55] and [12,24,35,24,88,120,155]
    Write a program to make a list whose elements are intersection of the above given lists.  
"""

print(set([1,3,6,78,35,55]).intersection(set([12,24,35,24,88,120,155])))

"""
Code Challenge
  Name: 
    Duplicate
  Filename: 
    duplicate.py
  Problem Statement:
    With a given list [12,24,35,24,88,120,155,88,120,155]
    Write a program to print this list after removing all duplicate values 
    with original order reserved  
"""

list1=list(set([12,24,35,24,88,120,155,88,120,155]))
print(list1[::-1])


"""
Code Challenge
  Name: 
    Mailing List
  Filename: 
    mailing.py
  Problem Statement:
  I recently decided to move a popular community  mailing list (3,000 subscribers, 
  60-80 postings/day) from my server to Google Groups. 
  I asked people to joint he Google-based list themselves, 
  and added many others myself, as the list manager. 
  However, after nearly a week, only half of the list had been moved. 
  I somehow needed to learn which people on the old list hadn't yet 
l  signed up for the new list.


  Fortunately, Google will let you export a list of members of a group to 
  CSV format. 
  Also, Mailman (the list-management program I was using on
  my server) allows you to list all of the e-mail addresses being used 
  for a list. Comparing these lists, I think, offers a nice chance to look
  at several different aspects of Python, and to consider how we can 
  solve this real-world problem in a "Pythonic" way.


  The goal of this project is thus to find all of the e-mail addresses on 
  the old list that aren't on the new list. The old list is in a file 
  containing one e-mail address per line, as in:
    
  Hint:
      Refer to mailing.txt for the new and old list of email addresses.
      
"""

old_list = set(["janusfury@aol.com",
"ajlitt@me.com",
"dburrows@me.com",
"robles@yahoo.com",
"jshirley@gmail.com",
"saridder@live.com",
"dmiller@mac.com",
"agapow@yahoo.ca",
"hamilton@sbcglobal.net",
"madler@att.net",
"grady@gmail.com",
"iami@gmail.com",
"heroine@gmail.com",
"loxy@att.net",
"violinhi@icloud.com",
"morain@sbcglobal.net",
"rgiersig@gmail.com",
"jhardin@outlook.com",
"pappp@msn.com",
"hermanab@live.com",
"avollink@verizon.net",
"bulletin@yahoo.com",
"smallpaul@msn.com",
"wagnerch@hotmail.com",
"harryh@me.com",
"gbacon@live.com",
"jcholewa@yahoo.ca",
"thassine@sbcglobal.net",
"amky@me.com",
"mgreen@gmail.com",
"srour@icloud.com",
"heidrich@gmail.com",
"danzigism@me.com",
"sabren@mac.com",
"arebenti@sbcglobal.net",
"marcs@live.com",
"shrapnull@att.net",
"jguyer@mac.com",
"msherr@me.com",
"aaribaud@aol.com",
"mfleming@yahoo.com",
"seano@icloud.com",
"laird@icloud.com",
"manuals@live.com",
"mfburgo@live.com",
"budinger@optonline.net",
"udrucker@verizon.net",
"benits@outlook.com",
"baveja@mac.com",
"feamster@gmail.com"])

new_list = set(["violinhi@icloud.com",
"morain@sbcglobal.net",
"rgiersig@gmail.com",
"jhardin@outlook.com",
"pappp@msn.com",
"hermanab@live.com",
"avollink@verizon.net",
"bulletin@yahoo.com",
"smallpaul@msn.com",
"wagnerch@hotmail.com",
"harryh@me.com",
"gbacon@live.com",
"jcholewa@yahoo.ca",
"thassine@sbcglobal.net",
"amky@me.com",
"mgreen@gmail.com",
"srour@icloud.com",
"heidrich@gmail.com",
"danzigism@me.com",
"sabren@mac.com",
"arebenti@sbcglobal.net",
"marcs@live.com",
"shrapnull@att.net",
"jguyer@mac.com",
"msherr@me.com",
"aaribaud@aol.com",
"mfleming@yahoo.com",
"seano@icloud.com",
"laird@icloud.com",
"manuals@live.com",
"mfburgo@live.com",
"budinger@optonline.net",
"udrucker@verizon.net",
"benits@outlook.com",
"baveja@mac.com",
"feamster@gmail.com"])
third=old_list.difference(new_list)
print(third)

