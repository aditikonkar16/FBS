#1.Structure ()
tu= (10,20,20,30,3.14,'abc')
#tu = (10,)
#print(type(tu))

#2.Hetrogeneous
#3.Ordered
#4.Immutable
#5.Duplication allowed
#tu [0] = 50 #raise error
#print(type(tu))
#print(tu)
#6. Tuple is faster than list bcoz the 
import sys
tu=()
li=[]
print(sys.getsizeof(tu))
print(sys.getsizeof(li))
