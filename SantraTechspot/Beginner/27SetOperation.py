#  'add', 'clear', 'copy', 'difference ( - ) ', 'difference_update', 'discard', 'intersection ( & )', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference ( ^ )', 'symmetric_difference_update', 'union ( | )', 'update'

# add off
a = {1,2,3,4}
print("\n \t add off ")
a.add(5)
print(a)
# clear off
print("\n \t clear off ")
a.clear()
print(a)

# copy off
b={10,20,30}
print("\n \t copy off ")
c=b.copy()
print(b)
b.add(50)
print(b)
print(c)

# difference off
print("=====> Using Function <=====")
print("\n difference off ")
d = {1, 2, 3, 4}
e = {1, 2, 5, 6}
print(d.difference(e))
print(e.difference(d))

# difference_update off
print("\n difference_update off ")
d.difference_update(e)
print(d) # Here update the difference at d
print(e)

print("=====> Using Symbols <=====")
f = {1,2,3,4}
g = {1, 2, 5, 6}
print(f-g)
print(g-f)

# union off
print("\n union off ")
print("=====> Using Function <=====")
print(f.union(g))
print(g.union(f))
print("=====> Using Symbols <=====")
print(f | g)
print( g | f)

# intersection off
h= {1,2,3,4}
i = {1,2,5,6}
print("\n intersection off ")
print("=====> Using Function <=====")
print(h.intersection(i))
print(i.intersection(h))
print("=====> Using Symbols <=====")
print(h & i)
print( i & h)

# intersection_update off
print("\n intersection_update off ")
h.intersection(i)
i.intersection(h)
print(h)
print(i)

# isdisjoint ==> Both set values is different or no commen values means return True else Flase
print("\n isdisjoint off ")
j = {1,2,3,4}
k = {5,6,7}
print(j.isdisjoint(k))
l = {1, 5, 6, 7}
print(j.isdisjoint(l))

# issubset Check the both set values any values as commen return True else False
print("\n\t issubset off ")
m= {1,2,3}
n = {1, 2, 3, 4, 5}
print(m.issubset(n))
o = {4,5,7}
print(m.issubset(o))

# issuperset off
print("\n\t issuperset off ")
p = {1, 2, 3, 4, 5, 6, 7, 8}
q = {1,2,3,4,5}
print(p.issuperset(q))
print(q.issuperset(p))

# pop off --> Remove the first values of set
print("\n\t pop off")
r = {10,20,30,50}
print(r.pop())

# remove off --> it's take one arg , which value you want to remove
print("\n\t remove off ")
print(r.remove(50))


# Symmtric_difference --> return non-common values in both set  [ ^ --> Cup Operator ]

s = {1, 2, 4}
t = {1, 5, 6}
print("\n\t symmentric_difference ")
print(s ^ t)
print(s.symmetric_difference(t))

# Symmtric_difference_update
print("\n\t symmentric_difference_update ")
u = {2,3,1,5,6}
v = {5, 6, 2, 9, 0}
print(u)
u.symmetric_difference_update(v)
print(u)

# discard  --> Remove the specified items , this method doesn't raise any error if the specified element is not present in the set

fruit = {"apple", "banana", "cherry"}
fruit.discard("banana")
fruit.discard("anana")
print(fruit)

# update --> Update the set with the union of this set and others

x = {"apple", "cherry"}
y={"google","microsoft"}
x.update(y)
print(x)