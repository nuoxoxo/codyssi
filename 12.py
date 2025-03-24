lines = open(0).read().splitlines()
print('part 1/',sum(len([_ for _ in l if _.isalpha()]) for l in lines))

def f(a,counthyphen=False):
    def alphahyphen(c) -> bool:
        return c.isalpha() or c == '-' if counthyphen else c.isalpha()
    while 42:
        i = 0
        found = False
        while i < len(a) - 1:
            l,r = i,i+1
            while l > -1 and r < len(a) and alphahyphen(a[l]) and a[r].isnumeric()\
                or l > -1 and r < len(a) and alphahyphen(a[r]) and a[l].isnumeric():
                a[l],a[r] = None,None
                l,r = l-1,r+1
                found = True
            l,r = i,i+1
            if found:
                break
            i += 1
        if not found:
            break
        a = [_ for _ in a if _ is not None]
    return a

A = [list(_) for _ in lines]
print('part 2/',sum([len(f(_[:],True)) for _ in A]))
print('part 3/',sum([len(f(_[:],False)) for _ in A]))
