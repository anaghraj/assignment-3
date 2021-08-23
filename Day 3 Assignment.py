def div(a,b):
    print(a/b)


def mod_div(fun):
    def inner(a,b):
        if(a<b):
            a,b=b,a
        fun(a,b)
    return(inner)

f=mod_div(div)
f(2,4)