
def fib(n):
    """ Compute fibonacci numbers recursively. """
    if n < 0 or n%1 != 0:
        print 'n should be a positive integer.'
    elif n == 0:
        return 0
    elif n < 3:
        return 1
    else:
        return fib(n-1)+fib(n-2)

### Is this a good way to do this? ###

def table(m):
    """ Lets collect some data. """
    l = []
    print 'n\telapsed(s)'
    for n in range(m):
        import time
        start = time.time()
        #print start
        fib(n)
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


# this takes a couple min to run, but it is so worth it!
if __name__ == '__main__':
    l = table(39)
    sillyplot(l)
    print "i'm exponential!"
    
    
