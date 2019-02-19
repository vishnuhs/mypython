hours=float(input('enter hours\n'))
rate=float(input('enter rate\n'))
if(hours>40):
    pay=(40*rate)+(hours-40)*(rate)*1.5
    print(pay)
else:
    pay=hours*rate
    print(pay)

