def add_string(str1):
  length = len(str1)

  if length > 2:
    if str1[-3:] == "ing":
      str1 += "ly"
    else:
      str1 += "ing"

  return str1

str1=input("enter string:")
print(add_string(str1))
