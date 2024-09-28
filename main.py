n =int(input("enter your number : "))
flag = True
for i in range( 2,n ) :
    if(n%i==0) :
        flag = False
        break
if (flag==True) :
    print("the number is prime")
else :
    print("the number is composite")