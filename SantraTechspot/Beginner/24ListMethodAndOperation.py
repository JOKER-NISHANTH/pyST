#print(dir(list))

# 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'
l = [1,2,3,4,5,6]
print(len(l))
print(max(l))
print(min(l))

n = "Nishanth"
print("\n",n, " ", type(n))
m = list(n)
print("\n", m, " ", type(m))


L = []
for i in range(20):
    if i % 2 == 0:
        L.append(i)
print(L)

LI = [10, 20, 10, 20, 30, 40, 50, 60]
c = LI.count(10)
print(c)

# Extend Syntax
L.extend(LI)
print("\n", L)
print("\n", LI)

# Insert Syntax  listObject.insert(pos,value)
Insert = [11, 22, 33, 44, 55]
Insert.insert(6, 66)
print(Insert)

# Pop --> Default_Index(-1)
P = Insert.pop()
print(P)

# Remove -->  Values
Insert.remove(33)
print(Insert)

# Reverse
Insert.reverse()
print(Insert)

# Sorting

Insert.sort()
print(Insert)