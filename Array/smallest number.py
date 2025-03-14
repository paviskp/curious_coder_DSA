a=[5,7,34,67,2,56,5,8]
n=len(a)
small=a[0]
for i in range(n):
    if(small>a[i]):
        small=a[i]
print(small)
