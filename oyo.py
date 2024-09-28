starting = int(input("enter the starting value : "))
ending= int(input("enter your ending value"))
for i in range(starting, ending+1) :
    flag = True
    for j in range(2, i ) :
        if (i%j==0) :
            flag = False
            break
    if (flag==True) :
            print(i)