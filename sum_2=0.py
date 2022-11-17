'''Write a Python program to sum of three given integers. However, if
two values are equal sum will be zero'''


x=int(input("enter a given value:"))
y=int(input("enter a given value:"))
z=int(input("enter a given value:"))
if x==y or y==z or x==z:
    print("sum:",0)
else:
    print("sum:",x+y+z)

   

