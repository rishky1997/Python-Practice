#3.Write python program to check  that given email address is valid or not?

import re
s=input('Enter Email address:')
o=re.findall('[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}',s)
if o==[s]:
    print('Email is valid')
else:
    print('Email is not valid')
