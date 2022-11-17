

"""
Negative Indexing:

Negative Indexing is used to in Python to begin slicing
from the end of the string i.e. the last.
Slicing in Python gets a sub-string from a string.
The slicing range is set as parameters i.e. start, stop and step.


e.g:
"""

print("Negative Indexing".center(80,"*"))
print()
print()
#  012345678901234567   (for positive)
s="tops career center"
#  876543210987654321   (for negative)


print("positive_slicing".center(80,"*"))
print(s[5:11])
print("Negative_slicing".center(80,"*"))
print(s[-13:-7])
print(s[::-1])
