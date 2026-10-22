def add(*data):
    sum=0
    for val in data:
        sum+=val
    return sum
res = add(10,20,30,40,1,2,3,4,5,6,7,8,9)
print(res)