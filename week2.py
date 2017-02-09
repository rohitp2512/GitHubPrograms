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
