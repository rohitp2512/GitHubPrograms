#Armstrong number
def arm(n):
	n1=n
	sum=0
	while n1!=0:
		d=n1%10
		sum+=(d*d*d)
		n1=int(n1/10)
	if sum==n:
		print(n,"is an Armstrong number")
	else :
		print(n,"is not an Armstrong number")
		
arm(153)
arm(35)
arm(123)
arm(371)
arm(999)