def TreeList(r):
    return [r,[],[]]

def insertLeft(root,newVal):

    t = root.pop(1)
    if len(t)>1:
        root.insert(1,[newVal,t,[]])
    else:
        root.insert(1,[newVal,[],[]])

def insertRight(root,newVal):

    t = root.pop(2)
    if len(t) > 1:
        root.insert(2,[newVal,[],t])

    else:
        root.insert(2,[newVal,[],[]])

def getRoot(root):
    return root[0]

def setRoot(root,newRoot):
    root[0] = newRoot

def getLeft(root):
    return root[1]

def getRight(root):
    return root[2]

r = TreeList(5)
insertRight(r,3)
insertRight(r,8)
insertRight(r,22)
insertRight(r,32)
insertLeft(r,43)
insertRight(r,432)
insertLeft(r,21)
insertLeft(r,11)
print(getLeft(r))
print(r)
print(r[2])
