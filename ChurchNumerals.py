def zero(f):
    return lambda x: x


def one(f):
    return lambda x: f(x)


def two(f):
    return lambda x: f(f(x))


def succ(cn):
    return lambda f: lambda x: f(cn(f)(x))

def sum(cn1, cn2):
    return lambda f: lambda x: cn1(f)(cn2(f)(x))

def prod(cn1, cn2):
    return lambda x: cn1(cn2(x))

def pred(cn):
    n = cnnum(cn)
    return lambda f: lambda x: repeat(f, n-1, x)

def increment(x): return x+1

def cnnum(cn):
    return cn(lambda x: x+1)(0)

def repeat(f,n,x):
    if (n == 1):
        return f(x)
    else:
        return repeat(f, n-1, f(x))

def numcn(n):
    return lambda f: lambda x: repeat(f,n,x)


three = succ(two)
four = succ(three)
print("Testing cnnum")
print(cnnum(one))
print(cnnum(two))
print("Testing successor")
print(cnnum(succ(one)))
print(cnnum(succ(succ(zero))))
print("Testing product")
print(cnnum(prod(three, four)))
print(cnnum(prod(four, three)))
print(cnnum(prod(three, one)))
print("Testing sum")
print(cnnum(sum(three, four)))
print(cnnum(sum(one, one)))
print("Testing numcn")
print(cnnum(numcn(2)))
print(cnnum(numcn(5)))
print("Testing pred")
print(cnnum(pred(numcn(5))))
print(cnnum(pred(succ(two))))











