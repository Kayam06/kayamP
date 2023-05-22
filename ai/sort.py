x = []

n = int(input("Enter how many elements you want for sorting"))

for i in range(n):
    print("Enter list elements")
    a = int(input(""))
    x.append(a)

print("unsorted Elements list is: ", x)

for i in range (0,len(x)-1):
     for j in range (i + 1, len(x)) :
        if x[i]>x[1]:
            c = x[i]    
            x[i] = x[j] 
            x[j]=c
print("Sorted Elements List is: ",x)