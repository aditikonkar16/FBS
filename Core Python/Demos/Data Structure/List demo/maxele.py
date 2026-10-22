li =[45,60,23,50,60,90,31,100]
max=li[0]
for ind in range(1,len(li)):
    if(li[ind]> max):
        max=li[ind]
print('Max:',max)