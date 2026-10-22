#method1
def sq(n):
    return n*n

data=[1,2,3,4,5,6,7,8,9,10]
res = list(map(sq,data))
print(res)

#method2
def sq(n):
    return n*n

res = list(map(lambda n:n*n,data))
print(res)