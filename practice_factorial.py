#Write a Python program to get the Factorial number of given number

#by while loop to show factorial no.



a=int(input("enter a value:"))
fac=1
while a>0:
    fac=fac*a
    a=a-1
print("factorial:",fac)



#by if/else + for loop to show factorial no.
#a=int(input("enter a value:"))
#fac=1
"""if a<0:
    print("no factorial for negetive no.")
elif a==0:
    print("factorial is 1")
else:
for a in range(1,a+1):
    fac=fac*a
    a=a+1
print("factorial is :",fac) """       
