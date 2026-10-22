def sumofSeries(n):
    if (n <= 1):
        return 0
    else:
        return n + sumofSeries(n - 1)
    
    n=5
    res=sumofSeries(n)
    print(res)