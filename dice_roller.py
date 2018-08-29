from random import randint

min = 1
max = 6

roll = "y"

while roll == "yes" or "y":
    print ("rolling your dice...")
    print (randint(min,max) , randint(min,max))

    roll = input("do it again??")
    if roll == "y":
        continue
    else:
        break