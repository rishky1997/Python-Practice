numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
neven=0
nodd=0
for i in numbers:
    if i%2==0:
        neven+=1
    else:
        nodd+=1
print('Number of even numbers :',neven)
print('Number of odd numbers :',nodd)
