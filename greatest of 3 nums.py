a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
c=int(input("Enter the third number:"))

#Using a user-built function
#Uses if..elif..else.. conditional statements
def greaternum(x,y,z):
    if (x>y & x>z):
        print("first number is greatest")
    elif(y>x & y>z):
            print("second number is greatest")
    else:
            print("third number is greatest")

greaternum(a,b,c)

#Another Method
#using Nested if

#def greaternum():
    #if (a>b):
        #if (a>c):
            #print("first number is greatest")
        #else:
            #print("third number is greatest")
    #else:
        #if(b>c):
            #print("second number is greatest")
        #else:
            #print("third number is greatest")
