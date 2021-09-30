def gcd(x,y):
    while(y):
        x,y = y,x%y
    return x
lst=list(map(int,input().split()))
g=gcd(lst[0],lst[1])
for i in range(2,len(lst)):
    g=gcd(g,lst[i])

for i in range(1,g+1):
    if(g%i==0):
        print(i)
        