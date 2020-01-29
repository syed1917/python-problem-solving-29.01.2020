import random
a=int(input("enter the number:"))
b=random.randrange(0,20)
if(a==b):
    print("winner",a,b)
else:
    print("better luck next time")

'''
enter the number:19
better luck next time

enter the number:17
better luck next time
'''
