#1.Python program to Swap Keys and Values in Dictionary.

d={
    1:'one',
    2:'two',
    3:'three'
}
d=dict([(j,i) for i,j in d.items()])
print(d)
