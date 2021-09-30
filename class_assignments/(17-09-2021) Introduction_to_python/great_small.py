#PROGRAM       : Find the possible largest and smallest number with given numbers
#PROGRAMMED BY : Badam Jwala Sri Hari
#MAIL ID       : jwalasrihari1330@gmail.com
#DATE          : 17-09-2021
#PYTHON VERSION: 3.9.7
#CAVEATS       : None
#LICENSE       : None


n=list(map(int,list(input())))

#Sorting the list 
#converting every element to string because join method accepts only string object 
n=list(map(str,sorted(n)))

#joining the sorted elements
s="".join(n)

#As the sorted method sorts in ascending order we have to reverse the string to get greatest number
print("Greatest number:",s[::-1])

#joined string is directly printed
print("Smallest number:",s)
