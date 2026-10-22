def binarySearch(li,search_ele):
    beg=0
    end=len(li)-1
    while(beg<=end):
        print('beg:',beg)
        print('end:',end)
        mid=(beg+end)//2
        print('mid:',mid)
        if(search_ele==li[mid]):
            return mid
        elif(search_ele<li[mid]):
            end=mid-1
        elif(search_ele>li[mid]):
            beg=mid+1
    else:
        return -1
    
li=[10,20,30,40,50,60,]
res = binarySearch(li,30)
if(res!=-1):
    print(f'{30} is present at index {res}')
else:
    print(f'{30} is not present')
    
