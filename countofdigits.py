n=int(input('no:'))
count=0
while(n>0):
    ld=n%10
    count=count+1
    n=n//10
print(count)
