# Set
#print(dir(set))
#  'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update'

# Set is used remove the duplicate
# Set has no Index_Value
a = {1, 2, 3, 4}
print("\n\t",a," ", type(a))
a = {}
print("\n\t",a, " ", type(a))
a = set()
print("\n\t", a, " ", type(a))

# Adding in Set
b=set()
b.add(10)
b.add(20)
print("\n\t", b, " ", type(b))

# Removing function in Set --> Discard , Pop , Remove , Clear

Set = {11, 22, 33, 44, 55, 66}
print("\n\t", Set, " ", type(Set))
Set.remove(55)
print("\n\t -----> After Removing  <----- \n\t", Set, " ", type(Set))
print("\n \t In Set Pop  Removing first Value only ")
Set.pop()
print("\n\t -----> After Pop  <----- \n\t", Set, " ", type(Set))
Set.discard(2)
print("\n\t -----> After Discard  <----- \n\t", Set, " ", type(Set))
Set.clear()
print("\n\t -----> After Clear  <----- \n\t", Set, " ", type(Set))