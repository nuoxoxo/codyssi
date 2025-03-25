A,B = open(0).read().split('\n\n')
d = {}
for a in A.splitlines():
    l,_,r = a.split()
    d[l] = int(r)
def p1(d,B):
    for b in B.splitlines():
        _,l,_,r,_,amt = b.split()
        d[l] -= int(amt)
        d[r] += int(amt)
    print('part 1/',sum(sorted(list(d.values()))[-3:]))
def p2(d,B):
    for b in B.splitlines():
        _,l,_,r,_,amt = b.split()
        pay = min(d[l],int(amt))
        d[l] -= pay
        d[r] += pay
    print('part 2/',sum(sorted(list(d.values()))[-3:]))

p1(dict(d),B)
p2(dict(d),B)

e = {}
for k,v in d.items():
    e[k] = [v,[]]#,defaultdict(dict)] # a debtee's debt wont accumulate - FIXME

def roundpay():
    while 42:
        found = False
        for k,(bal,Q) in e.items():
            if bal > 0 and Q: # has $ and debtees
                debtee,deb = Q[0]
                pay = min(bal,deb)
                e[k][0] -= pay
                e[debtee][0] += pay
                if Q[0][1] == 0:
                    Q.pop(0)
                else:
                    Q[0][1] = deb - pay
                found = True
            if found:
                break
        if not found: # no payable debt
            break
for b in B.splitlines():
    _,l,_,r,_,amt = b.split()
    amt = int(amt)
    pay = min(e[l][0],amt)
    e[l][0] -= pay
    e[r][0] += pay
    if amt > pay:
        e[l][1].append([r, amt - pay])
    roundpay()

print('part 3/',sum(sorted([v[0] for v in e.values() if not v[1]])[-3:]))
