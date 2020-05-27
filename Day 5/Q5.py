'''
5.Iterate a given list and check if a given element already exists in a       
dictionary as a key’s value if not delete it from the list.
roll_number = [47, 64, 69, 37, 76, 83, 95, 97]
sampledict = {“John”:47,”Peter”:64,”Mahi”:37,”Maria”:76}
'''

roll_number = [47, 64, 69, 37, 76, 83, 95, 97]
sampledict = {"John":47,"Peter":64,"Mahi":37,"Maria":76}
l=[]
for i in roll_number:
    if i in sampledict.values():
        l.append(i)
roll_number=l
print(roll_number)
