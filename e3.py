s=input('enter score\n')
try:
    score=float(s)
    if(1.0>=score>=0.9):
        print('A')
    elif(0.9>score>=0.8):
        print('B')
    elif(0.8>score>=0.7):
        print('C')
    elif(0.7>score>=0.6):
        print('D')
    elif(0.6>score>0.0):
        print('F')
    else:
        print('Enter proper score')
except:
    print('Enter proper score')

