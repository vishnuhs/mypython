def comp(a,b,c):
    high,mid,low=0,0,0
    if a>b and a>c:
        high=a
    if b>a and b>c:
        high=b
    if c>a and c>b:
        high=c
    if a>b and a<c or a<a and a>c:
        mid=a
    if c>b and c<a or c<b and c>a:
        mid=c
    if b>a and b<c or b<a and b>c:
        mid=b
    if a<b and a<c:
        low=a
    if b<a and b<c:
        low=b
    if c<a and c<b:
        low=c
    print(high>mid>low)
    return high,mid,low


