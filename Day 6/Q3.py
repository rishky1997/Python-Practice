#3.Write program to implement Insertion sort.


no=[25,17,31,13,2]
l=len(no)
for i in range(1,l): 
        key = no[i] 
        j = i-1
        while j >=0 and key < no[j] : 
                no[j+1] = no[j] 
                j -= 1
        no[j+1] = key

print(no)
