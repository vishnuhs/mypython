h=input('enter hours\n')
try:
    hours=float(h)
    r=input('enter rate\n') 
    rate=float(r)
    if(hours>40):
        pay=(40*rate)+(hours-40)*(rate)*1.5
        print(pay)
    else:
        pay=hours*rate
        print(pay)
except:
    print('please enter a number')
