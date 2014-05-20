
# Can you do this with recursion?
# lucas
def luc(n): #F_n = F_n-1 + F_n-2; F_1 = 2, F_2 = 1
    a,b,c = 2,1,0
    if n == 1:
        return 2
    elif n == 2:
        return 1
    else:
        for i in range(n-2):
            c = a+b
            a = b
            b = c
        return c

# fibonacci
def fib(n): #F_n = F_n-1 + F_n-2; F_1 = 1, F_2 = 1
    a,b,c = 1,1,0
    if n == 1 or n == 2:
        return 1
    else:
        for i in range(n-1):
            c = a+b
            a = b
            b = c
        return c

### Is this a good way to do this? ###

def table(m,fibonacci=True):
    """ Lets collect some data. """
    l = []
    print 'n\telapsed(s)'
    for n in range(m):
        import time
        start = time.time()
        #print start
        if fibonacci: fib(n)
        else: luc(n)
        elapsed = time.time() - start
        print n,'\t',elapsed
        l.append(elapsed)
    return l

def sillyplot(l):
    M = len(l)
    m = M
    #l.reverse()
    for x in range(M):
        space = M
        p = []
        for y in l:
            y = int(round(y))
            if y >= m:
                space-=1
        p.append(' '*space+'*'*(M-space))
        print str(m)+' '*(2-len(str(m))),' '.join(p[0])
        m-=1
    p = ['  ']
    for x in range(M):
        p.append(' '*(2-len(str(x+1)))+str(x+1))
    print ''.join(p)

# m = 50 works well for a test
def run2n(m):
    #n = int(raw_input("enter n as an integer to find the nth fibonacci and lucas number:\n")
    for n in range(m):
        print "the n=",n," fibonacci number is: ",fib(n)
        print "the n=",n," lucas number is:     ",luc(n)

if __name__ == '__main__':
    # try this out
    l = table(100)
    sillyplot(l)
    # my god, sillyplot doesn't even work the response is so fast
    # the uglier code wins!

