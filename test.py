a = [i for i in range(1,50+1)]
b = [i for i in range(50,100+1)]
c = [i for i in range(100,150+1)]
d = [i for i in range(150,200+1)]
e = [i for i in range(200,250+1)]
f = [i for i in range(250,300+1)]
g = [i for i in range(300,350+1)]
h = [i for i in range(350,400+1)]
i = [i for i in range(400,450+1)]
j = [i for i in range(500,550+1)]

zz = a,b,c,d,e,f,g,h,i,j

for i in zz:
    for b in i:
        print(b)




#/////////////////////////////////////////////////////////




for a in range(1,3000+1):
    print(a)







#///////////////////////////////////////////////////////



avg = 0

while avg != 20.0:
    score = input("Enter your score with comma: ")
    
    counter = 0
    scores = score.split(",")
    
    for i in scores:
        counter+= int(i) 
    avg = counter / len(scores)


print("I will buy a bike for you")






#/////////////////////////////////////////////////////////////




pass1 = input("Enter your password => ")
pass2 = input("Enter your password again => ")

if pass1 == pass2:
    print("The entered passwords are the same")
else:
    print("wrong password")







#///////////////////////////////////////////////////////////////////


