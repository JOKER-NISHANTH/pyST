# Immutable Object
#print(dir(tuple))
# 'count', 'index'
# 'del' , 'min' , 'max' , 'len'

T = tuple()
print("\n", T, " ", type(T))

t = (11, 33, 55,33)
print("\n", t, " ", type(t))

# How to Add a  Values in Tuples
t = t + (66,)
print("\n", t, " ", type(t))
print("\n", " " ,t[0])
print("\n", " " ,t[2:])
print("\n", " ", t[::-1])
#del(t)
# print("\n", " ", t) # NameError: name 't' is not defined

Tuple = (9, 7, 2000)
print(Tuple)
for i in Tuple:
    print(i)
print("Length of Tuple ",len(Tuple))
print("Max of Tuple ",max(Tuple))
print("Min of Tuple",min(Tuple))
print("Count in Tuple",t.count(33))
# Index Syntax ---> Tuple-Object.index(value,start,stop)
print("Index in  Tuple",t.index(33,2))

# Adding two Tuples

t1 = (1,2,3,4,5)
t2=(6,7,8,9,0)
at=t1+t2
print("Adding two Tuple",at)
print("Adding two Tuple",at*2)

MT = ((1, 2), (3, 4), (5, 6))
for i ,j in MT:
    print("I-->",i,"J-->",j)
