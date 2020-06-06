#2.Write python program to check  that given number is valid mobile number or not?

import re
s=input('Enter mobile no.')
o=re.findall('[7-9][0-9]{9}',s)
if o==[s]:
    print('No. is valid')
else:
    print('No. is not valid')
