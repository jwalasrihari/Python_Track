#PROGRAM       : Find the possible largest and smallest number with given numbers
#PROGRAMMED BY : Badam Jwala Sri Hari
#MAIL ID       : jwalasrihari1330@gmail.com
#DATE          : 28-09-2021
#PYTHON VERSION: 3.9.7
#CAVEATS       : None
#LICENSE       : None


n=list(map(int,list(input())))
n=list(map(str,sorted(n)))
s="".join(n)
print("Greatest number:",s[::-1])
print("Smallest number:",s)