a=int(input("enter your choice: \n1:Odd\n2:Even\n3:Div by 3\n4:Div by 5\n"))
if(a==1):
    for i in range(1,50):
        if(i%2!=0):
            print(i)
elif(a==2):
    for i in range(1,50):
        if(i%2==0):
            print(i)
elif(a==3):
    for i in range(1,50):
        if(i%3==0):
            print(i)
elif(a==4):
    for i in range(1,50):
        if(i%5==0):
            print(i)
else:
    print("error")
    
'''    
enter your choice:   
1:Odd
2:Even
3:Div by 3
4:Div by 5
1
1
3
5
7
9
11
13
15
17
19
21
23
25
27
29
31
33
35
37
39
41
43
45
47
49

enter your choice: 
1:Odd
2:Even
3:Div by 3
4:Div by 5
2
2
4
6
8
10
12
14
16
18
20
22
24
26
28
30
32
34
36
38
40
42
44
46
48

enter your choice: 
1:Odd
2:Even
3:Div by 3
4:Div by 5
3
3
6
9
12
15
18
21
24
27
30
33
36
39
42
45
48

enter your choice: 
1:Odd
2:Even
3:Div by 3
4:Div by 5
4
5
10
15
20
25
30
35
40
45  
'''
   
   
  
