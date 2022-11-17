def reverse_string(str1):
    if len(str1) % 4 == 0:
       return "".join(reversed(str1))
    return str1


str1=input("enter value:")
print(reverse_string(str1))

