#PROGRAM       : Find the Common factor of all elements in list
#PROGRAMMED BY : Badam Jwala Sri Hari
#MAIL ID       : jwalasrihari1330@gmail.com
#DATE          : 17-09-2021
#PYTHON VERSION: 3.9.7
#CAVEATS       : None
#LICENSE       : None


#method to find GCD of given two numbers
def gcd(x,y):
    while(y):
        x,y = y,x%y
    return x

lst=list(map(int,input().split()))
g=gcd(lst[0],lst[1])

#iterating over the list and find the GCD
for i in range(2,len(lst)):
    g=gcd(g,lst[i])

    
#factors of GCD of all elements
for i in range(1,g+1):
    if(g%i==0):
        print(i)
        
