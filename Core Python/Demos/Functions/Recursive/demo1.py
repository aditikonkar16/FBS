def fun(n):
    print('function executing')
    if(n>1):
        fun(n-1)
n=5
fun(n)