def perm(l1,l2):
    if len(l1) is not len(l2):
        return False
    else:
        if sorted(l1) == sorted(l2):
            return True

l= perm('clint eastwood','old west action')
print((sorted('clint abc')))
print((sorted('cl i n t abc')))
print(l)
