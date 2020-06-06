#4.Write a python program to check given car registration number is valid Maharashtra state registration number or not?

import re
s=input('Enter car registration number:')
o=re.findall('^MH[0-9]{2}[A-Z]{2}[0-9]{4}$',s)
if o==[s]:
    print('No. is valid')
else:
    print('No. is not valid')
