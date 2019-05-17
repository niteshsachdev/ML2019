j=1
while(j<101):
    if (j%3)==0 and (j%5)!=0:
        print("Fizz")
    elif (j%5)==0 and (j%3)!=0:
        print("Buzz")
    elif (j%5)==0 and (j%3)==0:
        print("FizzBuzz")
    else:
        print(j)
    j=j+1