def bill(d):
    cost=d*7
    print("cost of per kilometer is Rs.7 \n your cost for travelling is ",cost)
a=int(input("enter your place to travel from poonamalle: \n1:central\n2:retteri\n3:redhills \n"))
if(a==1):
    bill(25)
elif(a==2):
    bill(15)
elif(a==3):
    bill(35)

else:
    print("invalid")

'''
enter your place to travel from poonamalle: 
1:central
2:retteri
3:redhills 
1
cost of per kilometer is Rs.7 
 your cost for travelling is  175
 
 enter your place to travel from poonamalle: 
1:central
2:retteri
3:redhills 
2
cost of per kilometer is Rs.7 
 your cost for travelling is  105
 
 enter your place to travel from poonamalle: 
1:central
2:retteri
3:redhills 
3
cost of per kilometer is Rs.7 
 your cost for travelling is  245
 '''
