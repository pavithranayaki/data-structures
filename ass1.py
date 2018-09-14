def intreverse(p):
    l=''
    p=str(p)
    for i in p:
        l=i+l
    l=int(l)
    return l
def matched(s):
    stack=[]
    for i in s:
        if i=='(':
            stack.append(i)
        elif i==')':
            if len(stack):
                stack.remove('(')
    if len(stack)>0:
        return False
    else:
        return True
      
def factors(n):
    factorslist=[]
    for i in range(1,n+1):
        if n%i==0:
            factorslist=factorslist+[i]
    return(factorslist)
  
def isprime(n2):
    return(factors(n2)==[1,n2])
def sumprimes(n3):
    primelist=0
    for j in n3:
        if isprime(j):
            primelist=primelist+j
    return primelist
	#print(sumprimes(5))
