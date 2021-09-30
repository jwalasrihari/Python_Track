#PROGRAM       : Find the sum of two numbers without doing carry forward 
#PROGRAMMED BY : Badam Jwala Sri Hari
#MAIL ID       : jwalasrihari1330@gmail.com
#DATE          : 17-09-2021
#PYTHON VERSION: 3.9.7
#CAVEATS       : None
#LICENSE       : None


#func takes two numbers and return a number by suming without carry forward
def func(n,m):
    j=-1
    ans=""
    ln=len(n)
    lm=len(m)
    min_length=min(ln,lm)
    for i in range(min_length):
        
        #moving from the last and adding digits
        #but taking only one digit from last and adding to ans variable
        temp=str(int(n[j])+int(m[j]))[-1]
        ans+=temp
        j-=1
    
    #if both digits are of different length we have to add extra part to ans
    #adding remaining part to ans with was not iterated in above for loop
    if ln<lm:
        ans+="".join(m[:lm-min_length][::-1])
    elif lm<ln:
        ans+="".join(n[:ln-min_length][::-1])
    print(ans[::-1])
    
    
n=list(map(str,list(input())))
m=list(map(str,list(input())))
func(n,m)
