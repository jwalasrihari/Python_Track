#PROGRAM DESCRIPITON: Take a 4 digit number non-repeating number and arrange it in ascending and descending order to get two new numbers.
#                     Then subtract the highest number from lower number till you get the number 6147.
#                     If the end result is 6147 then return TRUE else FALSE.


# PROGRAMMED BY: B Jwala Sri Hari
# MAIL ID : jwalasrihari1330@gmail
# DATE    : 17-09-2021
# VERSION : 3.7.9
# CAVEATS : None
# LICENSE : None



def great_small(p):
    p=list(map(str,sorted(p)))
    s="".join(p)
    print("Greatest number:",s[::-1])
    print("Smallest number:",s)
    print("-------------------------")
    return int(s[::-1]),int(s)

n=list(map(int,list(input())))
store=[]
h,l=great_small(n)
while(1):
    h,l=great_small(list(str(h-l)))
    temp=h-l
    if temp in store:
        print("FALSE")
        break
    if temp==6174:
        print("TRUE")
        break
    store.append(temp)
    
    
