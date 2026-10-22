def linearSearch(li,search_ele):
    for ind in range(0,len(li)):
        if(search_ele == li[ind]):
            return ind
    else:
        return -1
    
li =[56,23,96,78,88,55,34]
ele=int(input('enter element:'))
res=linearSearch(li,ele)
if(res!=-1):
    print(f'{ele} is at index {res}')
else:
    print(f'{ele} is not present')