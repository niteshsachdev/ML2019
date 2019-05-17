string='RESTART'
index=string.index('R')
string1=string
string2=string1[index+1:].replace('R','$')
print(string[:index+1]+string2)