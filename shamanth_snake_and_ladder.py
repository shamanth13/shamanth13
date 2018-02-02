import random
count=0
while(count<=100):
    n=input("enter r to roll the dice")#r is the random dice number which the computer generates
    if(n=='r'):
        r=random.randint(1,6)
        count=count+r
        print("your random is",r)
        print("your count is",count)
        if(count==8):
            count+37
            print("climb the ladder",count)#climbing the ladder
        elif(count==13):
            count=34
            print("climb the ladder",count)
        elif(count==40):
            count=68
            print("climb the ladder",count)
        elif(count==52):
            count=81
            print("climb the ladder",count)
        elif(count==76):
            count=87
            print("climb the ladder",count)
        elif(count==11):
            count=2
            print("snake bites",count)#snake bites
        elif(count==25):
            count=4
            print("snake bites",count)
        elif(count==89):
            count=70
            print("snake bites",count)
        elif(count==93):
            count=64
            print("snake bites",count)
        elif(count==100):
            print("you are the winner")#if you get 100 then you are the winner
            break
        elif(count>100):
            count=count-r
            print("try again")#if it is more than 100 then try again
        else:
            print("continue to play")
 
