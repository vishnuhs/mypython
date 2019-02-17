def comp(a,b,c):
    if a>b:
        if a>c:
            max=a
            if b>c:
                min=c
                mid=b
            else:
                min=b
                mid=c
        else:
            max=c
            mid=a
            min=b
    else:
        if b>c:
            max=c
            if c>a:
                mid=c
                min=a
            else:
                mid=a
                min=c
        else:
            min=a
            mid=b
            max=c
    return max,mid,min
