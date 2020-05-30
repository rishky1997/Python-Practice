#5. Write a Python program to square and cube every number in a given list of integers using Lambda. 
l=[1,2,3,4,5,6,7,8,9,10,11]
s=list(map(lambda x:x*x,l))
c=list(map(lambda x:x*x*x,l))
print('Squares:',s)
print('Cubes:',c)
