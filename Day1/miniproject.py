# Challenge 1
import random
r1 = random.randint(0,10)
print (r1)
j=0
while j<7:
    num=int(input("Enter the number"))
    diff=num-r1
    if (num>-1):
        if r1==num:
            print("YOU WIN")
            break
        else:
            print("COMPUTER WINS")
            #Challenge 2
            print("Random number {} and guess number {}".format(r1,num))
            if diff>3 and diff<5:
                print("Guess is Too low")
            elif diff>5 and diff<8:
                print("Guess is Too High")
    else:
        print("Enter positive integer")
    j=j+1

