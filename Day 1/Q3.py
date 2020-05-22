l=[]
print("Enter a String:")
while True:
    s=input()
    l.append(s)
    if s=="":
        break
for i in l:
    print(i.upper())
