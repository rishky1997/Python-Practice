#4. Write a program to count how many reference variables in a program. 

import sys
a=1111
b=1111
c=a
d=b
print(sys.getrefcount(a))
