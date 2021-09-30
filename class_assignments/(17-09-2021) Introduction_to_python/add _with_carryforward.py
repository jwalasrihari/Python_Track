def func(n,m):
    j=-1
    ans=""
    ln=len(n)
    lm=len(m)
    min_length=min(ln,lm)
    for i in range(min_length):
        temp=str(int(n[j])+int(m[j]))[-1]
        ans+=temp
        j-=1
    if ln<lm:
        ans+="".join(m[:lm-min_length][::-1])
    elif lm<ln:
        ans+="".join(n[:ln-min_length][::-1])
    print(ans[::-1])

n=list(map(str,list(input())))
m=list(map(str,list(input())))
func(n,m)