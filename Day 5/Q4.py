'''
4.Write a python program to concatenate two lists index-wise.
List1 = [“M”,”na”,”i”,”lak”]
List2 = [“y”,”me”,”s”,”han”]
Expected output:
[“My”,”name”,”is”,”lakhan”]
'''



List1 = ["M","na","i","lak"]
List2 = ["y","me","s","han"]
l=[]
for i in range(len(List1)):
    l.append(List1[i]+List2[i])
print(l)
