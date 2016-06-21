


#Define the Iterator
a = [1,2,3,4,5,6]
b = [1,2,3]
c = [1,2,3,4,5]
d = [1]

master =[]
master.append(a)
master.append(b)
master.append(c)
master.append(d)


totalElements = len(a) + len(b) + len(c) + len(d)

map = dict()
map[tuple(a).__hash__()] = (0,len(a))
map[tuple(b).__hash__()] = (0,len(b))
map[tuple(c).__hash__()] = (0,len(c))
map[tuple(d).__hash__()] = (0,len(d))

processedElements = 0


def hasNext():
    
    return processedElements < totalElements

def next():
    
    pass 
