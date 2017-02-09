#Function1 intreverse of 'n' takes an integer value and reverses the digits and displays the output
# intreverse(456) will display an output 654
# intreverse(0980) will display an output 0890
#Function2 matched(s)
#Write a function matched(s) that takes as input a string s and checks if the brackets "(" and ")" in s
#are matched: that is, every "(" has a matching ")" after it and every ")" has a matching "(" before it. 
#Your function should ignore all other symbols that appear in s.  Your function should return 
#True if s has matched brackets and False if it does not.
#>>> matched("zb%78")
#True
#>>> matched("(7)(a")
#False
#>>> matched("a)*(?")
#False
#>>> matched("((jkl)78(A)&l(8(dd(FJI:),):)?)")
#True

#Function3 sumprimes(a)
#Write a function sumprimes(l) that takes as input a list of integers and retuns the sum of all the prime numbers in l.
#Here are some examples to show how your function should work.
#
#>>> sumprimes([3,3,1,13])
#19
#>>> sumprimes([2,4,6,9,11])
#13
#>>> sumprimes([-3,1,6])
#0

# Exception handling not done. Only pass required datatype values.

def intreverse(n):
	sum=0
	n1=n
	while n1!=0:
		d=n1%10
		sum=(sum*10)+d
		n1=int(n1/10)
	return(sum)
def matched(s):
    a=0
    b=0
    for i in range(0,len(s)):
        if s[i]=='(':
            a=a+1
        elif s[i]==')':
            b=b+1
        elif b>a:
            return(False)
    if a==b:
        return(True)
    else:
        return(False)
def prime(n):
    if n>1:
        for i in range(2,n):
            if n%i==0:
                return(False)
        return(True)
    else:
        return(False)
def sumprimes(a):
    sum=0
    for i in range(0,len(a)):
        b=prime(a[i])
        if b:
            sum=sum+a[i]
    return(sum)
