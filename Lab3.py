n=5
x=1
y=0
z=1
b=1
c=0
d=1
series='fibonacci'

if(series=='fibonacci'):
    for i in range(1,n+1):
        x=x+y
        a=x
        y=x+y
        if (n==1):
            print n,'st Fibonacci number:',n
            break
#        if(z<n):
#            print z,'th Fibonacci number:',x
        z=z+1
#        if(z<n):
#            print z,'th Fibonacci number:',y
        if(z>n):
            print n,'th Fibonacci number:',a
            break
        a=y
        z=z+1
        if(z>n):
            print n,'th Fibonacci number:',a
            break
elif(series=='sum'):
    for i in range(1,n+1):
        c=3*b
        e=d+c
        d=d+c
        b=b+1
    if(b==n+1):
        print '3*n + 3*(n-1) + 3*(n-2)...+ 1:',e
else:
    print 'Invalid string; enter valid string.'
    print 'Valid strings: fibonacci, sum'
    print 'Cause of error:','string','<',series,'>'
